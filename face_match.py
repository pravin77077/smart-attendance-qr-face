import cv2
import os
from deepface import DeepFace

dataset_path = "dataset"

cap = cv2.VideoCapture(0)

print("Press S to scan face")

while True:

    ret, frame = cap.read()
    cv2.imshow("Face Match", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):

        temp_image = "temp.jpg"
        cv2.imwrite(temp_image, frame)

        for file in os.listdir(dataset_path):

            db_img = os.path.join(dataset_path, file)

            try:
                result = DeepFace.verify(temp_image, db_img, enforce_detection=False)

                if result["verified"]:
                    print("Face Matched with:", file)
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()

            except:
                pass

        print("Face not recognized")

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()