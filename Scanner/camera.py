import cv2 
from pyzbar.pyzbar import decode
import time
from django.conf import settings
class VideoCamera(object):
        
        
    def get_frame(self):
        used=[]
        cap=cv2.VideoCapture(0)
        cap=cv2.VideoCapture(0)
        cap.set(3,640)
        cap.set(4,480)
        cv2.destroyAllWindows()
        f =cap.read()
        for code in decode(f):
            if(code.data.decode('utf-8') not in used):
                #print('approved')
                #code.type
                #print(decode(code))
                used.append(code.data.decode('utf-8'))
                return code.data.decode('utf-8')
                #used.append(code.data.decode('utf-8')
                time.sleep(5)
            elif(code.data.decode('utf-8') in used):
                
                return "sorry"
            time.sleep(5) 
                
        cv2.imshow("teeschgudd",f)
        cv2.waitKey(1)



