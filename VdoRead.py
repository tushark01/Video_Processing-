import cv2 

#vid_capture = cv2.VideoCapture('dhoom.mp4') #Video read n Play
vid_capture = cv2.VideoCapture(-1, cv2.CAP_DSHOW) #Video read from webCam

if (vid_capture.isOpened() == False):
	print("Error opening the video file")

while(vid_capture.isOpened()):
	
	ret, frame = vid_capture.read()
	if ret == True:
		cv2.imshow('Frame',frame)
		
		key = cv2.waitKey(20)
		
		if key == ord('q'):
			break
	else:
		break


vid_capture.release()
cv2.destroyAllWindows()