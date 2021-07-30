import os
from scipy.io import loadmat
import cv2
import numpy as np
root = r'F:\CV\research\dataset\video_text\JHMDB\mask_vis'
n_videos = 0
n_frames = 0
splits = os.listdir(root)
for split in splits:
    masks_clips_path = os.path.join(root, split)
    masks_clips = os.listdir(masks_clips_path)
    for mask_clip in masks_clips:
        n_videos += 1
        frames = os.listdir(os.path.join(masks_clips_path, mask_clip))
        n_frames += len(frames)
print(n_videos)
print(n_frames)
