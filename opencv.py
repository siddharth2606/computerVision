import pandas as pd
import cv2
import mediapipe as mp


#MediaPipe (hand Detection)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
p = mp_hands.Hands(static_image_mode= True,max_num_hands =2,min_detection_confidence= 0.5 )


while cap.isOpened():
    r, f = cap.read()
    f = cv2.flip(f,1)
    if r == True:
        img = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)

        result = p.process(f)


        f = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

        if result.multi_hand_landmarks:
            for landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(f,landmarks,
                                          mp_hands.HAND_CONNECTIONS)


        cv2.imshow("siddharth",f)
        if cv2.waitKey(25) & 0xff == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()


#MediaPipe (Face Detection)
# mp_face_det = mp.solutions.face_detection
# mp_draw = mp.solutions.drawing_utils


# face_dect = mp_face_det.FaceDetection(min_detection_confidence =0.5, model_selection = 0)
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     r, f = cap.read()
#     f = cv2.flip(f,1)

#     f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
#     result = face_dect.process(f)

#     f = cv2.cvtColor(f,cv2.COLOR_RGB2BGR)


#     if r == True:

#         for cr in result.detections:
#             mp_draw.draw_detection(f,cr)

#         cv2.imshow("siddharth",f)
#         if cv2.waitKey(25) & 0xff == ord("q"):
#             break
#     else:
#         break

# cap.release()
# cv2.destroyAllWindows()