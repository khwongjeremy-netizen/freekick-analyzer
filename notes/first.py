import pandas as pd
import numpy as np
import cv2
from glob import glob
import IPython.display as ipd
from tqdm.notebook import tqdm

import subprocess
input_file = ''
sub.process.run(['ffmpeg', '-1', input_file, -qscale, '0', '', '-loglevel', 'quiet'])

ipd.Video(' ',)
cap = cv2.videoCapture('')
#Total number of frames in video 
cap.get(cv2.cv2_PROP_FRAME_COUNT )

#Gets the height and width of the video
height = cap.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.getg(cv2.cv2.CAP_PROP_FRAME_WIDTH)
print(f'Height {height}, Width {width}')

#Get frame per second 
fps = cap.get(cv2.cv2.CAP_PROP_FPS)
print(f'FPS : {fps:0.2f}')

cap.release()

#Pulling images from a video
cap = cv2.VideoCapture('026c7465-309f6d33.mp4')
ret, img = cap.read()
print(f'Returned {ret} and img of shape {img.shape}')

#>> Displays images from videos 
## Helper function for plotting opencv images in notebook
def display_cv2_img(img, figsize=(10, 10)):
    img_ = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(img_)
    ax.axis("off")

display_cv2_img(img)
cap.release()

#Add annotations to videos and images
linkcode
labels = pd.read_csv('../input/driving-video-with-object-tracking/mot_labels.csv',
                     low_memory=False)
video_labels = (
    labels.query('videoName == "026c7465-309f6d33"').reset_index(drop=True).copy()
)
#Aligned with video frame rate
video_labels["video_frame"] = (video_labels["frameIndex"] * 11.9).round().astype("int")

video_labels["category"].value_counts()

''' Output: 

car              3030
pedestrian        847
bicycle           381
rider             320
truck             194
other vehicle     115
bus               109
other person       74
motorcycle         67
trailer            34
Name: category, dtype: int64
'''


def add_annotations(img, frame, video_labels):
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

'''
VIDEO_CODEC = "mp4v"
fps = 59.94
width = 1280
height = 720
out = cv2.VideoWriter("out_test.mp4",
                cv2.VideoWriter_fourcc(*VIDEO_CODEC),
                fps,
                (width, height))

cap = cv2.VideoCapture("026c7465-309f6d33.mp4")
n_frames = int(cap.get(cv2.cv2.CAP_PROP_FRAME_COUNT))

for frame in tqdm(range(n_frames), total=n_frames):
    ret, img = cap.read()
    if ret == False:
        break
    img = add_annotations(img, frame, video_labels)
    out.write(img)
out.release()
cap.release()
'''

