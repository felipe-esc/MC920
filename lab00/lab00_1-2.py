#!/usr/bin/python3

import sys, getopt
import cv2
import numpy as np

def brightness_adjust(image, gamma):
    image = image.astype(np.float32) / 255
    image = image ** (1/gamma)
    return (image * 255).astype(np.uint8)
    return 

def main(argv):
    input_img = ''
    output_img = ''
    gamma = -1
    try:
        opts, args = getopt.getopt(argv, "i:o:g:", ["input-file=","output-file=", "gamma="])
    except getopt.GetoptError:
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-i", "--input-file"):
            input_img = arg
        elif opt in ("-o", "--output-file"):
            output_img = arg
        elif opt in ("-g", "--gamma"):
            gamma = float(arg)

    if input_img == '':
        input_img = input('Input file path: ')
    if output_img == '':
        output_img = input('Output file name: ')
    if gamma == -1:
        gamma = float(input('Gamma: '))
    
    image = cv2.imread(input_img)
    if image is None:
        print ('Error opening image: ' + input_img)
        return -1

    cv2.imwrite(output_img, brightness_adjust(image, gamma))

if __name__ == "__main__":
    main(sys.argv[1:])
