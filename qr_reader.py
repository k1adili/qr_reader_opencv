# pip install opencv-python
# pip install pyzbar

import cv2
from pyzbar.pyzbar import decode
import pyclip
import winsound


try:
    # mobile or ipcam address
    url = "rtsp://192.168.1.200:8080/h264_pcm.sdp"

    cap = cv2.VideoCapture(url)

    camera, frame = cap.read()
    if frame is not None:
        cv2.imwrite('qr.png', frame)

    cv2.destroyAllWindows()

    img = cv2.imread('qr.png')
    code = decode(img)

    for barcode in decode(img):
        text = barcode.data.decode('utf-8')
        print(text)
        # copy to clipboard
        pyclip.copy(text)
        winsound.Beep(1000, 250)
except:
    winsound.Beep(500, 500)
    winsound.Beep(500, 500)
    winsound.Beep(500, 500)
    winsound.Beep(500, 1500)



