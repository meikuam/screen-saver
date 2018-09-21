import cv2
import datetime


def get_curr_time():
    date = datetime.datetime.now()
    today = str(date.year) + '-' + \
            str(date.month) + '-' + \
            str(date.day) + '_' + \
            str(date.hour) + ':' + \
            str(date.minute) + ':' + \
            str(date.second)
    return today

def cam_caputre(path):
    cam = cv2.VideoCapture(0)
    s, img = cam.read()

    if s:
        cv2.imwrite(path + get_curr_time() + '.png', img)