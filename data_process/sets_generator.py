import cv2
import os


SRC_PATH = './UChile_db_pascal_v0/Images'
#DST_PATH = './UChile_db_pascal_v0/New'

images = os.listdir(SRC_PATH)

f = open('./UChile_db_pascal_v0/test.txt','a')

for img in images:
	f.write(img[:-4] + '\n')

f.close()
