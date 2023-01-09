import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
# Define distortion coefficients

mtx =  np.array([[1010.53927637810, 0.000000, 946.461573216188],
                 [0.000000, 1011.10019447568, 531.836757099065],
                 [0.000000, 0.000000, 1.000000]])
dist = np.array([-0.346986059845099, 0.107344734262419, 0, 0, 0.000000])


def test():
	"""
	read the pickle file on disk and implement undistor on image
	show the oringal/undistort image
	"""
	print("Reading the sample image...")
	img = cv2.imread('D:\\2023\\01\\03\\camera_calibration\\record_files\\left\\out\\camera\\ins\\image_1671180017_1559339.jpeg')
	img_size = (img.shape[1],img.shape[0])
	print('img_size is',img_size)
	w = img_size[0]
	h = img_size[1]
	print("w is",w)
	newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1, (w,h))
	dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
	dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	# Visualize undistortion
	print("Visulize the result...")
	f, (ax1,ax2) = plt.subplots(2,1, figsize=(20,20))
	ax1.imshow(img), ax1.set_title('Original Image', fontsize=15)
	ax2.imshow(dst), ax2.set_title('Undistorted Image', fontsize=15)
	ax1.grid()
	ax2.grid()
	plt.show()
test()
