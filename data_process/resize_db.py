import cv2
import os


SRC_PATH = './UChile_db_pascal_v0/Images'
DST_PATH = './UChile_db_pascal_v0/New'

images = os.listdir(SRC_PATH)
#print(images)

img0 = cv2.imread(SRC_PATH+'/'+images[0])

print('Shape: {}'.format(img0.shape))

h,w,channels = img0.shape

if w > h:
	new_w, new_h = 640, 480
else:
	new_w, new_h = 480, 640

img0 = cv2.resize(img0,(new_w,new_h))


print('New Shape: {}'.format(img0.shape))

for img_name in images:
	img = cv2.imread(SRC_PATH+'/'+img_name)

	h,w,channels = img.shape

	if w > h:
		new_w, new_h = 640, 480
	else:
		new_w, new_h = 480, 640

	img = cv2.resize(img,(new_w,new_h))

	dst = DST_PATH+'/'+img_name[:-3]+'png'
	#print(dst)
	cv2.imwrite(dst,img)

print('=)!')