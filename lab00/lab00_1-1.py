#!/usr/bin/python3

import sys, getopt
import cv2
import numpy as np

def negative(img):
    return cv2.bitwise_not(img)

def vertical_mirror(img):
    return cv2.flip(img, 0)

def intensity_range(img):
    min_intensity = int(input("Min intensity: "))
    max_intensity = int(input("Max intensity: "))
    if min_intensity > max_intensity:
        print("Error: min cannot be greater than max!")
        exit()
    return ((img / 256) * (max_intensity - min_intensity)) + min_intensity

def odd_line_invertion(img):
    img[0::2, :] = img[0::2, ::-1]
    return img

def horizontal_reflection(img):
    img_height, img_width, c = img.shape

    img_top = img[0:int(img_height / 2), 0:img_width]
    img_bottom = cv2.flip(img_top, 0)

    return cv2.vconcat([img_top, img_bottom])

def main(argv):
    input_img = ''
    output_img = ''
    function_name = ''
    try:
        opts, args = getopt.getopt(argv, "i:o:f:", ["input-file=","output-file=", "function="])
    except getopt.GetoptError:
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-i", "--input-file"):
            input_img = arg
        elif opt in ("-o", "--output-file"):
            output_img = arg
        elif opt in ("-f", "--function"):
            function_name = arg

    if input_img == '':
        input_img = input('Input file path: ')
    if output_img == '':
        output_img = input('Output file name: ')
    if function_name == '':
        function_name = input('Function name: ')
    
    image = cv2.imread(input_img)
    if image is None:
        print ('Error opening image: ' + input_img)
        return -1

    if function_name == "negative":
        image = negative(image)
    elif function_name == "mirror":
        image = vertical_mirror(image)
    elif function_name == "range":
        image = intensity_range(image)
    elif function_name == "invert":
        image = odd_line_invertion(image)
    elif function_name == "reflect":
        image = horizontal_reflection(image)
    else:
        print("Error: function not found! Exiting!")
        return -1

    cv2.imwrite(output_img, image)

if __name__ == "__main__":
    main(sys.argv[1:])
