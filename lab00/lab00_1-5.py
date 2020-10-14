#!/usr/bin/python3

import sys, getopt
import cv2

def weighted_merge(image1, image2, weight):
    return ((image1 * weight) + (image2 * (1 - weight)))

def main(argv):
    input_img1 = input_img2 = output_img = ''
    weight = -1
    
    try:
        opts, args = getopt.getopt(argv, "f:s:o:w:", ["first-image=","second-image=","output-file=", "weight="])
    except getopt.GetoptError:
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-f", "--first-image"):
            input_img1 = arg
        elif opt in ("-s", "--second-image"):
            input_img2 = arg
        elif opt in ("-o", "--output-file"):
            output_img = arg
        elif opt in ("-w", "--weight"):
            weight = float(arg)

    if input_img1 == '':
        input_img1 = input('Input image 1 path: ')
    if input_img2 == '':
        input_img2 = input('Input image 2 path: ')
    if output_img == '':
        output_img = input('Output file name: ')
    if weight == -1:
        weight = float(input('Weight: '))
    
    image1 = cv2.imread(input_img1)
    if image1 is None:
        print ('Error opening image: ' + input_img1)
        return -1
    
    image2 = cv2.imread(input_img2)
    if image2 is None:
        print ('Error opening image: ' + input_img2)
        return -1

    if weight < 0 or weight > 1:
        print ('Weight must be between 0 and 1!')
        return -1

    cv2.imwrite(output_img, weighted_merge(image1, image2, weight).astype(int))

if __name__ == "__main__":
    main(sys.argv[1:])
