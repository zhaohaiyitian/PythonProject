import cv2
import mediapipe as mp

# 初始化MediaPipe的面部检测模块
mp_face = mp.solutions.face_mesh
face = mp_face.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 初始化视频捕获
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # 读取视频帧
    success, image = cap.read()
    if not success:
        break

    # 将图像从BGR转换为RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 处理图像并检测面部
    results = face.process(image_rgb)

    # 如果检测到面部，绘制关键点和连接线
    if results.multi_face_landmarks:
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing.draw_landmarks(
            image,
            results.multi_face_landmarks[0],
            mp_face.FACEMESH_CONTOURS,
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
        )

    # 显示处理后的图像
    cv2.imshow('Face Detection', image)

    # 按下'q'键退出
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()