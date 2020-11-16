#!/usr/bin/env python
# coding: utf-8

import cv2

image_path = "/home/rg-omen-1/catkin_ws/src/Ikeda/image/test/"
image = cv2.imread(image_path + "hama.jpg")

# Cannyフィルタを適用
image2 = cv2.Canny(image, 30, 200)

# ネガポジ反転
image2 = 256 - image2

# ファイルに保存
cv2.imwrite(image_path + "hama-canny.jpg", image2)
