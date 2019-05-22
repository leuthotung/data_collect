import cv2
import os
import time

capture_duration = 7

id = input("Enter your id: ") 
def video_to_frames(video, path_output_dir):
    # extract frames from a video and save to directory as 'x.png' where 
    # x is the frame index
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened() :
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '%d.png') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()


cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('{}.avi'.format(id),fourcc,20.0,(640,480))

start_time = time.time()
while( int(time.time() - start_time)< capture_duration):
    ret,frame = cap.read()
    cv2.imshow('frame',frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):   
        break
os.mkdir(id)
video_to_frames('{}.avi'.format(id),os.path.abspath(id))
cap.release()
out.release()
cv2.destroyAllWindows()