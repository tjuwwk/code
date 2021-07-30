import os
from scipy.io import loadmat
import cv2
import numpy as np
root = r'F:\CV\research\dataset\video_text\JHMDB\puppet_mask'
save_root = r'F:\CV\research\dataset\video_text\JHMDB\mask_vis'
if not os.path.exists(save_root):
    os.mkdir(save_root)
splits = os.listdir(root)
for split in splits:
    masks_clips_path = os.path.join(root, split)
    masks_clips = os.listdir(masks_clips_path)
    save_split = os.path.join(save_root, split)
    if not os.path.exists(save_split):
        os.mkdir(save_split)
    for mask_clip in masks_clips:
        masks_root = os.path.join(masks_clips_path, mask_clip, 'puppet_mask.mat')
        data = loadmat(masks_root)
        masks = data['part_mask']
        save_mask = os.path.join(save_split, mask_clip)
        if not os.path.exists(save_mask):
            os.mkdir(save_mask)
        for i in range(masks.shape[2]):
            mask = masks[:, :, i] * 255
            cv2.imwrite(os.path.join(save_mask, '%05d.png' % i), mask)
