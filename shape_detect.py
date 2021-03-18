# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# AIM
# desing as a function, and ruturn the shape

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import cv2

'''
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())
'''

# img = args["image"]
img = './red_tri_test.jpg'


def shape_detect(img):
	# load the image and resize it to a smaller images
	image = cv2.imread(img)
	imgae = imutils.resize(image, width=300)
	resized = imutils.resize(image, width=300)
	ratio = image.shape[0] / float(resized.shape[0])

	# convert the resized image to grayscale, blur it slightly, and threshold it
	gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

	# find contours in the thresholded image and initialize the shoape detector
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	sd = ShapeDetector()
	final_shape = []

	# loop over the contours
	for c in cnts:
		shape = sd.detect(c)
		final_shape.append(shape)


	triangle_number = shape.count('triangle')
	rectangle_number = shape.count('rectangle')
	circle_number = shape.count('circle')

	if triangle_number > rectangle_number:
		if triangle_number > circle_number:
			return 'triangle'
		else:
			return 'circle'

	elif rectangle_number > circle_number:
		return 'rectangle'

	elif circle_number > rectangle_number:
		return 'circle'

shape = shape_detect(img)
print(shape)