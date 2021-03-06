#!usr/bin/python3

import numpy as np

masks = {
    'floyd-steinberg': np.array([
        [0, 1, 7/16],
        [3/16, 5/16, 1/16]
    ]),
    'stevenson-arce': np.array([
        [0, 0, 0, 0, 1, 32/200, 0],
        [12/200, 0, 26/200, 0, 30/200, 0, 16/200],
        [0, 12/200, 0, 26/200, 0, 12/200, 0],
        [5/200, 0, 12/200, 0, 12/200, 0, 5/200]
    ]),
    'burkes': np.array([
        [0, 0, 1, 8/32, 4/32],
        [2/32, 4/32, 8/32, 4/32, 2/32]
    ]),
    'sierra': np.array([
        [0, 0, 1, 5/32, 3/32],
        [2/32, 4/32, 5/32, 4/32, 2/32],
        [0, 2/32, 3/32, 2/32, 0]
    ]),
    'stucki': np.array([
        [0, 0, 1, 8/32, 4/32],
        [2/32, 4/32, 8/32, 4/32, 2/32],
        [1/32, 2/32, 4/32, 2/32, 1/32]
    ]),
    'jarvis-judice-ninke': np.array([
        [0, 0, 1, 7/48, 5/48],
        [3/48, 5/48, 7/48, 5/48, 3/48],
        [1/48, 3/48, 5/48, 3/48, 1/48]
    ])
}