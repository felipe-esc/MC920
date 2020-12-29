#!/usr/bin/python3

import sys, getopt
import numpy as np
import cv2
import matplotlib.pyplot as plt
from math import exp

funcs = ["Global", "Bernsen", "Niblack", "Sauvola-Pietaksinen", "Phansalskar-More-Sabale", "Contrast", "Mean", "Median"]

def bernsen(nbrs):
    return (int(nbrs.min()) + int(nbrs.max())) / 2

def niblack(nbrs, k):
    return np.mean(nbrs) + k * np.std(nbrs) 

def sauvola_pietaksinen(nbrs, k, R):
    return np.mean(nbrs) + (1 + k * (np.std(nbrs) / R - 1))

def phansalskar_more_sabale(nbrs, k, p, q, R):
    mean = np.mean(nbrs)
    return mean + (1 + p * exp(-q * mean) + k * (np.std(nbrs) / R - 1))

def apply_filter(img):
    function = ""
    height, width = img.shape

    copy = img.copy()
    while function not in funcs:
        function = input("Choose between functions: \n [" + ', '.join(funcs) + "] \n")

    # get params
    if function == "Global":
        T = int(input("Insert a threshold: "))
        while T < 0 or T > 255:
            T = int(input("out of range[0, 255], try again: "))
    if function == "Niblack" or function == "Sauvola-Pietaksinen" or function == "Phansalskar-More-Sabale":
        k = float(input("Insert k: "))
        if function == "Sauvola-Pietaksinen":
            while k == 0:
                k = float(input("k must be different than 0: "))
    if function == "Sauvola-Pietaksinen" or function == "Phansalskar-More-Sabale":
        R = float(input("Insert R: "))
    if function == "Phansalskar-More-Sabale":
        p = float(input("Insert p: "))
        q = float(input("Insert q: "))

    # apply filter
    for i in range(1, height - 1):
        for j in range(1, width -1):
            if function != "Global":
                neighbors = img[i - 1 : i + 2, j - 1 : j + 2]
                neighbors = np.reshape(neighbors, (1, 9))
                neighbors = np.delete(neighbors, 4)
                
                if function == "Bernsen":
                    T = bernsen(neighbors)
                elif function == "Niblack":
                    T = niblack(neighbors, k)
                elif function == "Sauvola-Pietaksinen":
                    T = sauvola_pietaksinen(neighbors, k, R)
                elif function == "Phansalskar-More-Sabale": 
                    T = phansalskar_more_sabale(neighbors, k, p, q, R)
                elif function == "Mean":
                    T = np.mean(neighbors)
                elif function == "Median":
                    T = np.median(neighbors)
                # Contrast
                else:
                    ## close to min -> objt -> black
                    if abs(int(neighbors.min()) - img[i][j]) < abs(int(neighbors.max()) - img[i][j]):
                        T = 256
                    else:
                        T = 0

            if T < img[i, j]:
                pixel = 255
            else:
                pixel = 0
            copy[i][j] = pixel   

    return copy

def main(argv):
    input_img = ''
    output_img = ''
    hist = False
    
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input-file=","output-file=", "histogram"])
    except getopt.GetoptError:
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-i", "--input-file"):
            input_img = arg
        elif opt in ("-o", "--output-file"):
            output_img = arg
        elif opt in ("-h", "--histogram"):
            hist = True
    
    if input_img == '':
        input_img = input('Input file path: ')
    if output_img == '':
        output_img = input('Output file name: ')
    
    image = cv2.imread(input_img)
    if image is None:
        print ('Error opening image: ' + input_img)
        return -1
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if hist:
        plt.hist(image.flatten(),256,[0,256])
        plt.xlim([0,256])
        plt.savefig(output_img.partition(".png")[0] + "__hist.png")

    out = apply_filter(image)

    cv2.imwrite(output_img, np.int32(out))

if __name__ == "__main__":
    main(sys.argv[1:])
