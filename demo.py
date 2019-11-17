from mmdet.apis import init_detector, inference_detector, show_result
import mmcv
import os

config_file = 'configs/ttfnet/ttfnet_r18_1x.py'
checkpoint_file = 'checkpoints/ttfnet18_1x-fe6884.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image and show the results
#img = 'test1.png'  # or img = mmcv.imread(img), which will only load it once

#result = inference_detector(model, img)
#show_result(img, result, model.CLASSES)


imgs = ['test0.png', 'test1.png', 'test2.png','test3.png', 'test4.png', 'test5.png']
for i, result in enumerate(inference_detector(model, imgs)):
    show_result(imgs[i], result, model.CLASSES, out_file='result_{}.jpg'.format(i))