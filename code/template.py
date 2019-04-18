import numpy as np
import cv2

def saveFrame(event, x, y, flags, param):

    global frame

    print(x, y, flags, param)

    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('capture')
        cv2.imwrite('frame.png', frame)


cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')
font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    cv2.setMouseCallback('frame', saveFrame)

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.line(frame, (0, 150), (640, 150), (185, 128, 41), 10)
    # cv2.putText(frame,'text', (100, 130), font, 1, (255, 255, 255), 2)

    cv2.rectangle(frame, (170, 90), (470, 390), (0, 0, 0), 2)

    cv2.line(frame, (270, 90), (270, 390), (0, 0, 0), 2)
    cv2.line(frame, (370, 90), (370, 390), (0, 0, 0), 2)

    cv2.line(frame, (170, 190), (470, 190), (0, 0, 0), 2)
    cv2.line(frame, (170, 290), (470, 290), (0, 0, 0), 2)

    positions = {
    	(0, 0): (220, 140),
    	(0, 1): (320, 140),
    	(0, 2): (420, 140),
    	(1, 0): (220, 240),
    	(1, 1): (320, 240),
    	(1, 2): (420, 240),
    	(2, 0): (220, 340),
    	(2, 1): (320, 340),
    	(2, 2): (420, 340)
    }

    for pos in positions:
    	cv2.putText(frame,'n', (positions[pos][0] - 10, positions[pos][1] + 10), font, 1, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    # print(frame.shape)
    if cv2.waitKey(1) == 27:
        break
        

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


