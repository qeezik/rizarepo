import os
import cv2

# Check if OpenCV is installed
if not os.path.exists(cv2.__file__):
    print("OpenCV is not installed. Installing...")
    os.system("pip install opencv-python")

# Load the video file
video = cv2.VideoCapture('dance.mp4')

# Set the desired video size
video_size = (200, 100)  # width, height

# Create a window with a title
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video', video_size[0], video_size[1])

# Set the initial window position
window_x = 100
window_y = 100
cv2.moveWindow('Video', window_x, window_y)

while True:
    # Read a frame from the video
    ret, frame = video.read()
    
    # If the video ends, rewind it to the beginning
    if not ret:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = video.read()
    
    # Resize the frame
    frame = cv2.resize(frame, video_size)
    
    # Display the frame in the window
    cv2.imshow('Video', frame)
    
    # Get the current window position
    rect = cv2.getWindowImageRect('Video')
    window_x = rect[0]
    window_y = rect[1]
    
    # Check for keyboard events
    key = cv2.waitKey(1) & 0xFF
    
    # Move the window up
    if key == ord('w'):
        window_y -= 10
        cv2.moveWindow('Video', window_x, window_y)
    
    # Move the window down
    elif key == ord('s'):
        window_y += 10
        cv2.moveWindow('Video', window_x, window_y)
    
    # Move the window left
    elif key == ord('a'):
        window_x -= 10
        cv2.moveWindow('Video', window_x, window_y)
    
    # Move the window right
    elif key == ord('d'):
        window_x += 10
        cv2.moveWindow('Video', window_x, window_y)
    
    # Exit on key press
    elif key == ord('q'):
        break

# Release the video capture and close all windows
video.release()
cv2.destroyAllWindows()