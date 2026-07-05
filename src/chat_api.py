# FastAPI 问诊接口：TF-IDF 检索知识库 + Context 注入 Prompt + 调用大模型
@router.post("/chat")
async def chat(req: ChatRequest, current_user=Depends(get_current_user)):
    # 1. 用用户问题在本地辣椒病虫害知识库中检索 Top-K 相关条目
    sources = store.search(req.message, top_k=3)   # 内部使用 TF-IDF 向量 + 余弦相似度排序

    # 2. 将检索结果组织成可被大模型理解的上下文 Context
    context = "\n".join([
        f"【{i}】{doc['title']}（{doc['category']}）\n"
        f"症状：{doc['symptoms']}\n"
        f"原因：{doc['causes']}\n"
        f"防治：{doc['prevention']}\n"
        f"治疗：{doc['treatment']}"
        for i, (doc, score) in enumerate(sources, 1)
    ]) or "知识库暂无相关信息，请结合农业经验谨慎回答。"

    # 3. 构造系统 Prompt，将知识库检索结果作为上下文注入
    prompt = f"""
你是一名辣椒种植专家顾问，请基于下方知识库内容回答用户问题。
要求：判断病虫害类型，给出症状分析、防治建议、用药方式和安全间隔期。

【知识库 Context】
{context}
"""

    # 4. 将 Prompt 与用户问题一起发送给 OpenAI 兼容的大模型接口
    async with httpx.AsyncClient(timeout=180.0) as client:
        resp = await client.post(
            f"{LLM_API_BASE}/chat/completions",
            headers={"Authorization": f"Bearer {LLM_API_KEY}"},
            json={
                "model": LLM_MODEL,
                "messages": [
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": req.message}
                ],
                "temperature": 0.7,
            }
        )

    # 5. 返回大模型生成的问诊结果，并附带命中的知识库来源
    answer = resp.json()["choices"][0]["message"]["content"]
    return {"reply": answer, "sources": sources}
该接口采用轻量级 RAG 架构：后端首先基于 TF-IDF 与余弦相似度从辣椒病虫害知识库中检索最相关的症状、防治、用药条目，再将检索结果作为 Context 注入 Prompt，
最后调用 OpenAI 兼容大模型生成面向农户的问诊建议。
相比直接调用大模型，该方案能让回答更贴合本地知识库，减少幻觉，并保留可追溯的知识来源。
