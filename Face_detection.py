import cv2

# تحميل نموذج Haar Cascade للتعرف على الوجوه
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# فتح الكاميرا
cap = cv2.VideoCapture(0)

while True:
    # التقاط الإطار من الكاميرا
    ret, frame = cap.read()

    # تحويل الصورة إلى تدرجات الرمادي
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # اكتشاف الوجوه
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # رسم مستطيل حول الوجوه
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # عرض الصورة
    cv2.imshow('Face Detection', frame)

    # الخروج عند الضغط على "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# غلق الكاميرا والنوافذ المفتوحة
cap.release()
cv2.destroyAllWindows()