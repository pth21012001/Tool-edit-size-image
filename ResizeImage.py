import os 
import cv2 as cv 
import sys

filePath = sys.argv[1]
if os.path.exists(filePath):
	for r, d, f in os.walk(filePath):
		for file in f:
			if '.png' in file or '.jpg' in file and '.gif' not in file:
				img = cv.imread(filePath + "/" + file)
				img_resize = cv.resize(img, (64,64))
				new_path = filePath + "/resizeFolder"
				if not os.path.exists(new_path):
					os.mkdir(new_path)
				cv.imwrite(new_path + "/" + file, img_resize)
else:
	raise Exception("DUong truyen khong ton tai")

