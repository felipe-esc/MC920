#!/usr/bin/python3

import sys, getopt
import cv2
import numpy as np
from kernels import kernels

def combine_kernels(k1: np.ndarray, k2: np.ndarray):
    return np.sqrt(k1 ** 2 + k2 ** 2)

def main(argv):
    input_img = ''
    output_img = ''
    kernel_num = 0
    combine = False
    try:
        opts, args = getopt.getopt(argv, "i:o:k:c", ["input-file=","output-file=", "kernel=", "combine"])
    except getopt.GetoptError:
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-i", "--input-file"):
            input_img = arg
        elif opt in ("-o", "--output-file"):
            output_img = arg
        elif opt in ("-k", "--kernel"):
            kernel_num = int(arg)
        elif opt in ("-c", "--combine"):
            combine = True

    if input_img == '':
        input_img = input('Input file path: ')
    if output_img == '':
        output_img = input('Output file name: ')
    if (kernel_num <= 0 or kernel_num > 11) and not combine:
        kernel_num = input('Kernel (1,2,... 11): ')
    
    image = cv2.imread(input_img)
    if image is None:
        print ('Error opening image: ' + input_img)
        return -1
    if kernel_num > 11:
        print("Invalid kernel!")
        return -1

    if combine:
        # kernel = combine_kernels(kernels[2], kernels[3])
        temp1 = np.int32(cv2.filter2D(
                    image,
                    -1,
                    cv2.flip(kernels[2], -1)
                )) ** 2
        temp2 = np.int32(cv2.filter2D(
                    image,
                    -1,
                    cv2.flip(kernels[3], -1)
                )) ** 2
        out = np.sqrt(temp1 + temp2)
    else:
        kernel = kernels[kernel_num - 1]
        out = cv2.filter2D(
            image,
            -1,
            cv2.flip(kernel, -1)
        )
    
    cv2.normalize(np.int32(out), np.int32(out), 0, 255, cv2.NORM_MINMAX)

    cv2.imwrite(output_img, np.int32(out))

if __name__ == "__main__":
    main(sys.argv[1:])