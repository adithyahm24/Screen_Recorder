import cv2
import numpy as np
from PIL import ImageGrab

def screenrecorder():
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter('output.avi',fourcc,10,(1920,1080))
    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)

        out.write(frame)

        if cv2.waitKey(1) == 27:
            break
    out.release()
    cv2.destroyAllWindows()
screenrecorder()
