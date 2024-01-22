import cv2
import dlib
import matplotlib.pyplot as plt


# dlib’s HOG + Linear SVM face detector
detector = dlib.get_frontal_face_detector()


#%% Open CV Video Capture and frame analysis
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# The loop will break on pressing the 'q' key
while True:
    try:
        # Capture one frame
        ret, frame = cap.read()  
        
        # resizing for faster detection
        frame = cv2.resize(frame, (256, 256)) #Uncomment and see the speed up
        
        # Convert the image to grayscale (Dlib works with grayscale images)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        faces = detector(gray)
        
        for face in faces:
            x, y, w, h = (face.left(), face.top(), face.width(), face.height())
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        
        cv2.imshow("frame",cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))    
        
        if cv2.waitKey(10) == ord('q'):
           break
        
    
    except KeyboardInterrupt:
        break


cap.release()
cv2.destroyAllWindows()