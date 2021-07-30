import os
import cv2

videos_root = r'F:\CV\research\dataset\video_text\A2D\clips320H'
# train_splits = [f for f in os.listdir(data_root) if 'train' in f]
# train_split = os.listdir(data_root)
# for train_split in train_splits:
# videos_root = os.path.join(data_root, train_split)
videos = os.listdir(videos_root)
# save_split_root = os.path.join(os.path.join(data_root, train_split+'_imgs'))
save_root_all = r'F:\CV\research\dataset\video_text\A2D\Rename_Images'
if not os.path.exists(save_root_all):
    os.mkdir(save_root_all)
for video in videos:
    save_root = os.path.join(save_root_all, video.split('.')[0])
    if not os.path.exists(save_root):
        os.mkdir(save_root)
    vc = cv2.VideoCapture(os.path.join(videos_root, video))
    c = 0
    rval = vc.isOpened()
    while rval:
        c = c + 1
        rval, frame = vc.read()
        if rval:
            cv2.imwrite(save_root+'/%05d.png' % c, frame)  # 命名方式
            print(c)
        else:
            break
    vc.release()
