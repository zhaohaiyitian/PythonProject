import cv2
import mediapipe as mp

# 初始化MediaPipe的姿势检测模块
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 初始化视频捕获
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # 读取视频帧
    success, image = cap.read()
    if not success:
        break

    # 将图像从BGR转换为RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 处理图像并检测姿势
    results = pose.process(image_rgb)

    # 如果检测到姿势，绘制关键点和连接线
    if results.pose_landmarks:
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # 显示处理后的图像
    cv2.imshow('Pose Detection', image)

    # 按下'q'键退出
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()