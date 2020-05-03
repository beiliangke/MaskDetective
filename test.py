import cv2

detector = cv2.CascadeClassifier('data\\haarcascades\\haarcascade_frontalface_default.xml')
mask_detector = cv2.CascadeClassifier('data\\cascade.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in faces:
        # 参数分别为 图片、左上角坐标，右下角坐标，颜色，厚度
        face = img[y:y + h, x:x + w]  # 裁剪坐标为[y0:y1, x0:x1]
        mask_face = mask_detector.detectMultiScale(gray, 1.1, 5)
        for (x2, y2, w2, h2) in mask_face:
            cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)

    cv2.imshow('Cheney', img)
    cv2.waitKey(3)

cap.release()
cv2.destroyAllWindows()