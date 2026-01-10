import pandas as pd
import numpy as np
import cv2
from glob import glob
import IPython.display as ipd
from tqdm.notebook import tqdm
import subprocess


def display_cv2_img(img, figsize=(10, 10)):
    img_ = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(img_)
    ax.axis("off")

def anno(img, frame, video_labels):
    max_frame = video_labels.query("video_frame <= @frame")["video_frame"].max()
    frame_labels = video_labels.query("video_frame == @max_frame")
    for i, d in frame_labels.iterrows():
        pt1 = int(d["box2d.x1"]), int(d["box2d.y1"])
        pt2 = int(d["box2d.x2"]), int(d["box2d.y2"])
        #Creates coordinates for the box
        color = color_map[d["category"]]
        img = cv2.rectangle(img, pt1, pt2, color, 3)
        #creates a box around the image
    return img