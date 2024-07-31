import os
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
harcascade = os.path.join(os.getcwd(), "model", "haarcascade_russian_plate_number.xml")

if not os.path.isfile(harcascade):
    raise FileNotFoundError(f"Haar Cascade XML file not found at {harcascade}")

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

min_area = 500
count = 0

try:
    while True:
        success, img = cap.read()

        if not success:
            print("Failed to capture image")
            break

        plate_cascade = cv2.CascadeClassifier(harcascade)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

        for (x, y, w, h) in plates:
            area = w * h

            if area > min_area:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                img_roi = img[y: y + h, x:x + w]
                text = pytesseract.image_to_string(img_roi, config='--psm 7')
                cv2.putText(img, text.strip(), (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
                cv2.imshow("ROI", img_roi)

        cv2.imshow("Result", img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            save_path = os.path.join(os.getcwd(), "plates", f"scanned_img_{count}.jpg")
            cv2.imwrite(save_path, img_roi)
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 1)
            cv2.imshow("Results", img)
            cv2.waitKey(500)
            count += 1
        elif key == ord('q'):
            print("Quitting...")
            break

except KeyboardInterrupt:
    print("Program interrupted by user")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("Resources released and windows closed")
