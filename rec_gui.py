import time
import tkinter as tk
import cv2
import numpy as np
from PIL import ImageGrab


def screenrecorder():
    name = int(round(time.time() * 1000))
    name = 'Screenrecorded Videos\\{}.avi'.format(name)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(name, fourcc, 15, (1920, 1080))
    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        out.write(frame)

        if cv2.waitKey(1) ==32:
            break
    out.release()
    cv2.destroyAllWindows()
class recorder(tk.Tk):
    def __init__(self):
        super().__init__()
        self._frame = tk.Frame(self)
        self._frame.pack()
        l = tk.Label(self._frame, text="Screen Recorder", background='#F3D601')
        l.config(font=("Arial", 40, 'bold'))
        b = tk.Button(self._frame,
                      text = "Record",
                      command =self.record)

        l.grid(row = 0,column = 1)
        b.grid(row =2 ,column = 1)
    def record(self):
        self.iconify()
        screenrecorder()
        self.deiconify()

recorder().mainloop()