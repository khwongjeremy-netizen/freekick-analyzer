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

ret, img = cap.read()

cap.release()