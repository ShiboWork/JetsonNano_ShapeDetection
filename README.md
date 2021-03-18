# JetsonNano_ShapeDetection
A shape detection programe, which can be embedded into Jetson Nano. 

## Version 1
The version 1 is the original shape detection program. It can detect the target's simple shape on black background. The input is an image, while the output is the shape of input ('str'). The function is like classification network, but without training the network and only use the Opencv-python package.

USAGE:
1. Change the file path of the image. img = './image.jpg'
2. Enter 'python3 shape_detect.py'
