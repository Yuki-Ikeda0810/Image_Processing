#!/usr/bin/env python
# coding: utf-8

import cv2

image_path = "/home/rg-omen-1/catkin_ws/src/Ikeda/image/test/"
image = cv2.imread(image_path + "hama.jpg")

# グレイスケールに変換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ファイルに保存
cv2.imwrite(image_path + "hama-gray.jpg", gray)
