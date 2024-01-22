import cv2
import numpy as np
from skimage import feature
from skimage import exposure


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
        #frame = cv2.resize(frame, (140, 140)) #Uncomment and see the speed up
        
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        (H, hogImage) = feature.hog(image, orientations=9, pixels_per_cell=(8, 8),
    	cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1",
    	visualize=True)
        hogImage = exposure.rescale_intensity(hogImage, out_range=(0, 255))
        hogImage = hogImage.astype("uint8")
        hogImg = np.uint8(np.zeros((np.shape(hogImage)[0],np.shape(hogImage)[1],3)))
        hogImg[:,:,0] = hogImage
        hogImg[:,:,1] = hogImage
        hogImg[:,:,2] = hogImage
        
        catImg = cv2.hconcat([frame,hogImg])
        
        cv2.imshow("HOG Image", catImg)
        
        if cv2.waitKey(10) == ord('q'):
           break
        
    except KeyboardInterrupt:
        break

cap.release()
cv2.destroyAllWindows()