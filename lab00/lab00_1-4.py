#!/usr/bin/python3

import sys, getopt
import cv2
import numpy as np
import random

def mosaic(image):
    divisions = 4
    order = np.arange(divisions ** 2)
    height, width, c = image.shape

    random.shuffle(order)

    tiles_list = []
    tile_height = int(height / divisions)
    tile_width = int(width / divisions)

    for tile in order:
        line = tile % divisions
        column = int(tile / divisions)
        
        tiles_list.append(image[
                (line * tile_height) : ((line * tile_height) + tile_height),
                (column * tile_width) : ((column * tile_width) + tile_width)
            ])

    imgs_lines_gen = chunks(tiles_list, divisions)

    return cv2.vconcat([cv2.hconcat(imgs_line) for imgs_line in imgs_lines_gen])

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def main(argv):
    input_img = output_img = ''
    
    try:
        opts, args = getopt.getopt(argv, "i:o:", ["input-file=","output-file="])
    except getopt.GetoptError:
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-i", "--input-file"):
            input_img = arg
        elif opt in ("-o", "--output-file"):
            output_img = arg
        
    if input_img == '':
        input_img = input('Input file path: ')
    if output_img == '':
        output_img = input('Output file name: ')
    
    image = cv2.imread(input_img)
    if image is None:
        print ('Error opening image: ' + input_img)
        return -1

    cv2.imwrite(output_img, mosaic(image))

if __name__ == "__main__":
    main(sys.argv[1:])
