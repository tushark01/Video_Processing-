import cv2
#capture video from inbuit / external webcam and save into hardisk

#video = cv2.VideoCapture(0,cv2.CAP_DSHOW) #0 for inbuilt , 1 for external , we used cap_dshow because python 3.8 shows error for opencv
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#BIBX,XVID,MJPG,X264 AND WMV1, WMV2
#codec use only for video 

fourcc = cv2.VideoWriter_fourcc(*"XVID")
#it contains four parameter: first - Name, codec, fps, resolution

outpu = cv2.VideoWriter("videoweb2.avi", fourcc, 25, (640,420))
print(outpu)

while(video.isOpened()):
    ret,frame = video.read()
    if(ret==True):
        cv2.imshow("Game",frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        else:
            break
        
    cv2.waitKey(25)
video.release()
outpu.release()
cv2.destroyAllWindows()