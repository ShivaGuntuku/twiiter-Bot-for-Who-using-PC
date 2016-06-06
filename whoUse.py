"""Thanks for Helping Code """
import cv2
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#img_path = os.path.join(BASE_DIR,r'metaData\raw')
img_name = '{0}_{1}.{2}'.format('IMG',time.strftime('%d%m%y_%I%M%S'),'jpg')

def get_image():
	retval, im = camera.read()
	return im

camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)

for i in xrange(ramp_frames):
	temp = camera.read()

camera_capture = get_image()
filename = os.path.join(BASE_DIR,img_name)


def who():
	cv2.imwrite(filename, camera_capture)
	return filename

del(camera)

#s=who()
#print s