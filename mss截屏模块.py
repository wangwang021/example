import mss
import numpy as np
import cv2

#全屏截图
with mss.mss() as sct:  # 实例化mss
    # 截屏
    sct.shot(output='screenshot.png')
