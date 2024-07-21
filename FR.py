import cv2  
import numpy as np 
import dlib 
# from google.colab.patches import cv2_imshow 

# Connects computer's default camera 
cap = cv2.VideoCapture(0) # or link of video

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")
    exit() # Exit if camera cannot be opened 

# Detect the coordinates 
detector = dlib.get_frontal_face_detector()
  
# Capture frames continuously 
while True: 
  
    # Capture frame-by-frame 
    ret, frame = cap.read() 
    
    # Check if a frame was successfully read
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    frame = cv2.flip(frame, 1) 
  
    # RGB to grayscale 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces = detector(gray) 
  
    # Iterator to count faces 
    i = 0
    for face in faces: 
  
        # Get the coordinates of faces 
        x, y = face.left(), face.top() 
        x1, y1 = face.right(), face.bottom() 
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2) 
  
        # Increment iterator for each face in faces 
        i = i+1
  
        # Display the box and faces 
        cv2.putText(frame, 'face num'+str(i), (x-10, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2) 
        print(face, i) 
  
    # Display the frame 
    cv2.imshow(frame) # cv2_imshow for google collab
  
    # quit with the "q" button on a keyboard. 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
cap.release() 
cv2.destroyAllWindows()