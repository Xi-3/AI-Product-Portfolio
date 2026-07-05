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
