#!usr/bin/python3

import numpy as np

kernels = [
    # h1 - laplacian of gaussian
    np.array([[0, 0, -1, 0, 0],
              [0, -1, -2, -1, 0],
              [-1, -2, 16, -2, -1],
              [0, -1, -2, -1, 0],
              [0, 0, -1, 0, 0]]),
    # h2 - gaussian blur
    (1 / 256) * np.array([[1, 4, 6, 4, 1],
                          [4, 16, 24, 16, 4],
                          [6, 24, 36, 24, 6],
                          [4, 16, 24, 16, 4],
                          [1, 4, 6, 4, 1]]),
    # h3 - Right sobel                      
    np.array([[-1, 0, 1],
              [-2, 0, 2],
              [-1, 0, 1]]),
    # h4 - Bottom sobel         
    np.array([[-1, -2, -1],
              [0, 0, 0],
              [1, 2, 1]]),
    # h5 - Outline - passa alta
    np.array([[-1, -1, -1],
              [-1, 8, -1],
              [-1, -1, -1]]),
    # h6 - simple box blur - passa baixa   
    (1 / 9) * np.ones((3, 3)),
    # h7 - detecção diagonal
    np.array([[-1, -1, 2],
              [-1, 2, -1],
              [2, -1, -1]]),
    # h8 - same    
    np.array([[2, -1, -1],
              [-1, 2, -1],
              [-1, -1, 2]]),
    # h9 -  
    (1 / 9) * np.identity(9),
    # h10 -
    (1 / 8) * np.array([[-1, -1, -1, -1, -1],
                        [-1, 2, 2, 2, -1],
                        [-1, 2, 8, 2, -1],
                        [-1, 2, 2, 2, -1],
                        [-1, -1, -1, -1, -1]]),
    # h11 -       
    np.array([[-1, -1, 0],
              [-1, 0, 1],
              [0, 1, 1]])
]