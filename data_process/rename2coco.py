import cv2
import os


SRC_PATH = './UChile_db_news/Images_raw/'
DST_PATH = './UChile_db_news/Images/'

images = os.listdir(SRC_PATH)

idx = 0

for img_name in images:
    img = cv2.imread(SRC_PATH+img_name)
    

    if idx < 10:
        new_name = '0000000'+str(idx)+'.png'
    elif idx < 100:
        new_name = '000000'+str(idx)+'.png'
    elif idx < 1000:
        new_name = '00000'+str(idx)+'.png'

    print('new: {} | old: {}'.format(new_name,img_name))

    cv2.imwrite(DST_PATH+new_name,img)
    idx+=1





