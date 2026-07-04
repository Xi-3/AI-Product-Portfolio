# 刘熙茜 | AI 产品与增长运营作品集 🚀

> 懂底层算法逻辑的 AI 产品与增长运营。具备扎实的数据科学背景，熟练运用 Claude Code、Open Claw 等 AI 原生编程工具，致力于打造并运营有商业价值的 AI 产品生态。

### 🛠️ 核心武器库
`RAG 架构` `YOLOv8` `Python 全栈` `OpenClaw` `Claude Code` `数据驱动增长`

---

## 🤖 核心 AI 商业化与研发项目

### 项目一：辣椒智能防控问诊系统 (AI 产品化落地)
**核心技术**：`LLM API` `RAG` `FastAPI` `OpenClaw 辅助开发`

针对下沉市场病虫害诊断痛点，我独立设计并开发了专属图文知识库，完成了 AI 工具向 C 端产品的闭环转化。

![问诊社区多轮对话界面实机演示1](https://github.com/Xi-3/AI-Product-Portfolio/blob/main/86bb1ccd99fe6031a5bc3edba9519164.png?raw=true)
![问诊社区多轮对话界面实机演示2](https://github.com/Xi-3/AI-Product-Portfolio/blob/main/c553d36af14670803abab31e0555a352.png?raw=true)
![问诊社区多轮对话界面实机演示3](https://github.com/Xi-3/AI-Product-Portfolio/blob/main/33328754242c3da24dff980a0b4c5fc6.png?raw=true)
![问诊社区多轮对话界面实机演示4](https://github.com/Xi-3/AI-Product-Portfolio/blob/main/0176029f708d7b72e0e75b1b4f59e509.png?raw=true)

**技术亮点与实现：**
* **低幻觉知识检索**：基于 TF-IDF 与余弦相似度实现轻量级 RAG 检索工作流，极大降低了大模型幻觉。
* **Prompt 工程与 Context 注入**：将用户图片特征与知识库检索结果作为 Context 注入 Prompt，生成高准确率的拟人化诊断建议。

<details>
<summary>点击查看核心代码片段 (GPT-5.5 接入与 Context 注入)</summary>

```python
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
代码逻辑说明：该接口采用轻量级 RAG 架构：后端首先基于 TF-IDF 与余弦相似度从辣椒病虫害知识库中检索最相关的症状、防治、用药条目，再将检索结果作为 Context 注入 Prompt，最后调用 OpenAI 兼容大模型生成面向农户的问诊建议。相比直接调用大模型，该方案能让回答更贴合本地知识库，减少幻觉，并保留可追溯的知识来源。

项目二：病虫害 CV 监控及可视化大屏系统 (核心研发)
核心技术：YOLOv8 WebSocket Vue3 数据可视化

从业务场景出发，主导视觉模型推理部署与前端监控打通，构建了完整的物联网数据流与商业监控逻辑。

商业监控逻辑与技术闭环：

双通道通信低延迟推送：主导基于 YOLOv8 的目标检测模型推理部署，并将 AI 识别结果通过 WebSocket 实时推送到前端 Vue3 监控大屏。

数据驱动的业务决策：设计分级预警机制(Warning/Danger)，并结合温湿度传感器数据辅助决策干预，实现了软硬件数据的联动预警。

# 核心流程：YOLOv8 检测 + 分级预警 + WebSocket 实时推送
def analyze_frame(node_id: str, frame):
    # 1. YOLOv8 对视频帧进行病害目标检测
    results = yolo_model(
        frame,
        conf=CONF_THRESHOLD,   # 置信度阈值
        imgsz=IMG_SIZE,
        half=True,             # FP16 推理，降低服务器资源占用
        verbose=False
    )[0]

    # 2. 统计当前帧检测到的病害目标数量
    counts = {}
    for box in results.boxes:
        cls_name = yolo_model.names[int(box.cls)]
        counts[cls_name] = counts.get(cls_name, 0) + 1

    total = sum(counts.values())
    top_disease = max(counts, key=counts.get) if counts else "无"

    # 3. 根据检测数量进行分级预警
    if total >= ALERT_THRESHOLDS["danger"]:
        status = "danger"      # 危险：病害目标数量较多
    elif total >= ALERT_THRESHOLDS["warning"]:
        status = "warning"     # 预警：检测到一定数量病害
    else:
        status = "normal"      # 正常：未达到预警阈值

    payload = {
        "node_id": node_id,
        "counts": counts,
        "total": total,
        "top_disease": top_disease,
        "status": status,
        "timestamp": time.strftime("%H:%M:%S"),
    }

    # 4. 双通道通信：视频帧走 MJPEG，结构化检测结果走 WebSocket
    websocket.broadcast({"type": "nodes_update", "data": payload})

    # 5. 达到 Warning/Danger 时，额外推送报警事件给前端大屏
    if status in ("warning", "danger"):
        websocket.broadcast({"type": "alert", "data": payload})
项目的技术亮点：
YOLOv8 实时目标检测
按检测数量自动分级：normal / warning / danger
前端大屏通过 WebSocket 接收结构化结果
视频画面和检测数据分离传输：MJPEG + WebSocket 双通道通信

项目三： 📈 运营工作与实战：AI 赋能矩阵增长

 新媒体流量增长与自动化操盘 (独立负责)
运营周期：2025.02 - 2025.05 

独立负责抖音新账号的从 0 到 1 孵化，验证了高 ROI 的内容转化模型，并在后续业务中成功复用了该增长策略。

![单条爆款视频 2.9W+ 播放量实操截图](这里粘贴你那张 2.9w 播放量的图片链接)

*（图：零投放预算下，通过 A/B 测试动态优化前 3 秒完播率跑通的 2.9W+ 播放量单条爆款视频）*

增长策略与 AI 提效：
核心数据里程碑：在零投放预算下成功撬动自然流量池，累计斩获 “15万+” 曝光量，“单条爆款视频最高播放达 2.9万+（如上图实操截图所示）”，沉淀 “200+”深度互动(高赞/评论)。
算法破局与 A/B 测试：深入拆解平台推荐分发逻辑，基于 A/B 测试动态调整前 3 秒完播结构与互动钩子。
重构内容工作流：熟练利用各类 AI 工具与大模型重构工作流，实现竞品数据拆解、爆款脚本批量生成与自动化分发，显著缩短了创意到变现的流转周期。
