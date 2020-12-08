#!usr/bin/python3

import sys, getopt
import cv2
import numpy as np
import math

from masks import masks

def floyd_steinberg(img):
    m, n, d = img.shape

    for k in range(d):
        for i in range(1, m - 1):
            for j in range(1, n - 1):        
                if img[i, j, k] < 128:
                    g = 0
                else:
                    g = 1
                err = img[i, j, k] - g * 255

                # error distribution
                img[i + 1, j, k] = img[i + 1, j, k] + (7 / 16) * err
                img[i - 1, j + 1, k] = img[i - 1, j + 1, k] + (3 / 16) * err
                img[i, j + 1, k] = img[i, j + 1, k] + (5 / 16) * err
                img[i + 1, j + 1, k] = img[i + 1, j + 1, k] + (1 / 16) * err
    return img    

def color_apply(img, mask, alt):
    m, n, d = img.shape
    m_m, m_n = mask.shape # altura, largura
    invert = 1

    for k in range(d):
        for i in range(math.floor(m_n / 2) + 1, m - math.floor(m_n / 2)):
            for j in range(0, n - m_m, invert):
                g = -1

                if alt == True and i % 2 == 1:
                    invert = -1
                else:
                    invert = 1
                
                # iterate on mask
                for m_i in range(m_m): #(0, 3)
                    for m_j in range(0, m_n, invert): #(0,6)
                        # 0 = skip
                        if mask[m_i, m_j] == 0:
                            pass
                        # 1 = f(x,y)
                        elif mask[m_i, m_j] == 1:
                            if img[i, j, k] < 128:
                                g = 0
                            else:
                                g = 1
                            err = img[i, j, k] - g * 255
                        # distribute error
                        else:
                            offset = m_j - math.floor(m_n / 2)
                            # offset *= invert
                            x = i + offset
                            y = j + m_i
                            # apply error
                            img[x, y, k] = img[x, y, k] + mask[m_i, m_j] * err
    return img

def gray_apply(img, mask, alt):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    m_m, m_n = mask.shape
    m, n = img.shape
    invert = 1

    for i in range(math.floor(m_n / 2) + 1, m - math.floor(m_n / 2)):
        for j in range(0, n - (m_m - 1), invert):
            g = -1

            if alt == True and j % 2 == 1:
                invert = -1
            else:
                invert = 1
            
            # iterate on mask
            for m_i in range(m_m): #(0, 3)
                for m_j in range(0, m_n, invert): #(0,6)
                    # 0 = skip
                    if mask[m_i, m_j] == 0:
                        pass
                    # 1 = f(x,y)
                    elif mask[m_i, m_j] == 1:
                        if img[i, j] < 128:
                            g = 0
                        else:
                            g = 1
                        err = img[i, j] - g * 255
                    # distribute error
                    else:
                        offset = m_j - math.floor(m_n / 2)
                        # offset *= invert
                        x = i + offset
                        y = j + m_i
                        # apply error
                        img[x, y] = img[x, y] + mask[m_i, m_j] * err
    return img

def main(argv):
    input_img = ''
    output_img = ''
    option = ''
    alternate = False
    gray = False
    try:
        opts, args = getopt.getopt(argv, "gahi:o:m:", ["input-file=","output-file=", "mask=", "help", "gray"])
    except getopt.GetoptError:
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-i", "--input-file"):
            input_img = arg
        elif opt in ("-o", "--output-file"):
            output_img = arg
        elif opt in ("-m", "--mask"):
            option = arg
        elif opt in ("-a","--alternate"):
            alternate = True
        elif opt in ("-g","--gray"):
            gray = True
        elif opt in ("-h","--help"):
            print("Options:\n"
                + "    -i --input-file= -> input file path and file name with extension\n"
                + "    -o --output-file= -> outputfile path and file name with extension\n"
                + "    -m --mask= -> select mask\n"
                + "    -a --alternate -> apply mask alternating lines\n"
                + "    -g --gray -> converts colorized image to gray\n"
                + "Masks:\n"
                + "    'floyd-steinberg'\n"
                + "    'stevenson-arce'\n"
                + "    'burkes\n"
                + "    'sierra'\n"
                + "    'stuckis'\n"
                + "    'jarvis-judice-ninke'\n"
            )
            exit()
            
    
    while input_img == '':
        input_img = input('Input file path: ')
    while output_img == '':
        output_img = input('Output file name: ')
    while option == '':
        option = input('Select Mask: ')
    
    image = cv2.imread(input_img)
    if image is None:
        print ('Error opening image: ' + input_img)
        return -1
    if option not in masks:
        print('No mask found for that name, rerun with --help for more information.')
        return -1

    image = np.float32(image)

    # out = floyd_steinberg(image)
    if gray == True:
        out = gray_apply(image, masks[option], alternate)
    else:
        out = color_apply(image, masks[option], alternate)

    cv2.imwrite(output_img, np.int32(out))
    
if __name__ == "__main__":
    main(sys.argv[1:])
