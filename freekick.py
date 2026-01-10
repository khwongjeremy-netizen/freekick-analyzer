import pandas as pd
import numpy as np
import cv2
from glob import glob
import IPython.display as ipd
from tqdm.notebook import tqdm
import subprocess
import tkinter as tk
import func


kick_shot = cv2.VideoCapture('')
ret, img = cap.read()
func.display_cv2_img(img)
cap.release()
#Shot of the freekick's foot moment of impact


abels = pd.read_csv('',
                     low_memory=False)
video_labels = (
    labels.query('videoName == ""').reset_index(drop=True).copy()
)
video_labels["video_frame"] = (video_labels["frameIndex"] * 11.9).round().astype("int")



'''
Next task:
    -record clips of freekicks next time playing football
    -Test if I can annotate and pull images from clip



Goal: 
    -display the video on a window with tkinter
    -Calculate angles of freekicks(foot, ball, runup)