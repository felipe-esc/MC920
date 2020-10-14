#!/usr/bin/python3

import sys, getopt
import cv2
import numpy as np

def extract_bit_plan(image, bit_plan):
    return ((image >> bit_plan) & 1) * 255

def main(argv):
    input_img = output_img = ''
    bit_plan = -1
    
    try:
        opts, args = getopt.getopt(argv, "i:o:b:", ["input-file=","output-file=", "bit="])
    except getopt.GetoptError:
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-i", "--input-file"):
            input_img = arg
        elif opt in ("-o", "--output-file"):
            output_img = arg
        elif opt in ("-b", "--bit"):
            bit_plan = int(arg)

    if input_img == '':
        input_img = input('Input file path: ')
    if output_img == '':
        output_img = input('Output file name: ')
    if bit_plan == -1:
        bit_plan = int(input('Gamma: '))
    
    image = cv2.imread(input_img)
    if image is None:
        print ('Error opening image: ' + input_img)
        return -1
    if bit_plan < 0 or bit_plan > 7:
        print ('Bit plan must be a number between 0 and 7!')
        return -1

    cv2.imwrite(output_img, extract_bit_plan(image, bit_plan))

if __name__ == "__main__":
    main(sys.argv[1:])
