import cv2
import mediapipe as ma
import pyautogui as pg
cam = cv2.VideoCapture(0)
face_mesh = ma.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pg.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    op = face_mesh.process(rgb_frame)
    lm_points = op.multi_face_landmarks

    frame_h, frame_w, _ = frame.shape

    if lm_points:
        lms = lm_points[0].landmark

        for id, lm in enumerate(lms[474:478]):
            x = int(lm.x * frame_w)
            y = int(lm.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))

            if id == 1:
                screen_x = screen_w/frame_w * x
                screen_y = screen_h/frame_h * y
                pg.moveTo(screen_x, screen_y)
        left = [lms[145], lms[159]]
        for lm in left:
            x = int(lm.x * frame_w)
            y = int(lm.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004:
            pg.click()
            pg.sleep(1)
    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)
