import numpy as np
from PIL import Image
import random

pattern_range = {
    "1": [0,1],
    "2": [2,3],
    "3": [4,5],
    "4": [0,5],
}

algo_to_pixel = {
    "1": {
        0 : {
            "share1": [[[0, 255], [255, 0]], [[255, 0], [0, 255]], [[255, 0], [255, 0]], [[0, 255], [0, 255]], [[255, 255], [0, 0]], [[0, 0], [255, 255]]],
            "share2": [[[255, 0], [0, 255]], [[0, 255], [255, 0]], [[0, 255], [0, 255]], [[255, 0], [255, 0]], [[0, 0], [255, 255]], [[255, 255], [0, 0]],]
        },
        255: {
            "share1": [[[0, 255], [255, 0]], [[255, 0], [0, 255]], [[255, 0], [255, 0]], [[0, 255], [0, 255]], [[255, 255], [0, 0]], [[0, 0], [255, 255]]],
            "share2": [[[0, 255], [255, 0]], [[255, 0], [0, 255]], [[255, 0], [255, 0]], [[0, 255], [0, 255]], [[255, 255], [0, 0]], [[0, 0], [255, 255]]]
        }   
    },
    "2": {
        0 : {
            "share1": [[[0, 0, 255, 255], [255, 255, 0, 0]], [[255, 255, 0, 0], [0, 0, 255, 255]], [[255, 255, 0, 0], [255, 255, 0, 0]], [[0, 0, 255, 255], [0, 0, 255, 255]], [[255, 255, 255, 255], [0, 0, 0, 0]], [[0, 0, 0, 0], [255, 255, 255, 255]]],
            "share2": [[[255, 255, 0, 0], [0, 0, 255, 255]], [[0, 0, 255, 255], [255, 255, 0, 0]], [[0, 0, 255, 255], [0, 0, 255, 255]], [[255, 255, 0, 0], [255, 255, 0, 0]], [[0, 0, 0, 0], [255, 255, 255, 255]], [[255, 255, 255, 255], [0, 0, 0, 0]]]
        },
        255: {
            "share1": [[[0, 0, 255, 255], [255, 255, 0, 0]], [[255, 255, 0, 0], [0, 0, 255, 255]], [[255, 255, 0, 0], [255, 255, 0, 0]], [[0, 0, 255, 255], [0, 0, 255, 255]], [[255, 255, 255, 255], [0, 0, 0, 0]], [[0, 0, 0, 0], [255, 255, 255, 255]]],
            "share2": [[[0, 0, 255, 255], [255, 255, 0, 0]], [[255, 255, 0, 0], [0, 0, 255, 255]], [[255, 255, 0, 0], [255, 255, 0, 0]], [[0, 0, 255, 255], [0, 0, 255, 255]], [[255, 255, 255, 255], [0, 0, 0, 0]], [[0, 0, 0, 0], [255, 255, 255, 255]]]
        }
    },
    "3": {
        0 : {
            "share1": [[[0, 255, 0, 255], [255, 0, 255, 0]], [[255, 0, 255, 0], [0, 255, 0, 255]], [[255, 0, 255, 0], [255, 0, 255, 0]], [[0, 255, 0, 255], [0, 255, 0, 255]], [[255, 255, 255, 255], [0, 0, 0, 0]], [[0, 0, 0, 0], [255, 255, 255, 255]]],
            "share2": [[[255, 0, 255, 0], [0, 255, 0, 255]], [[0, 255, 0, 255], [255, 0, 255, 0]], [[0, 255, 0, 255], [0, 255, 0, 255]], [[255, 0, 255, 0], [255, 0, 255, 0]], [[0, 0, 0, 0], [255, 255, 255, 255]], [[255, 255, 255, 255], [0, 0, 0, 0]],]
        },
        255: {
            "share1": [[[0, 255, 0, 255], [255, 0, 255, 0]], [[255, 0, 255, 0], [0, 255, 0, 255]], [[255, 0, 255, 0], [255, 0, 255, 0]], [[0, 255, 0, 255], [0, 255, 0, 255]], [[255, 255, 255, 255], [0, 0, 0, 0]], [[0, 0, 0, 0], [255, 255, 255, 255]]],
            "share2": [[[0, 255, 0, 255], [255, 0, 255, 0]], [[255, 0, 255, 0], [0, 255, 0, 255]], [[255, 0, 255, 0], [255, 0, 255, 0]], [[0, 255, 0, 255], [0, 255, 0, 255]], [[255, 255, 255, 255], [0, 0, 0, 0]], [[0, 0, 0, 0], [255, 255, 255, 255]]]
        }
    },
    "4": {
        0 : {
            "share1": [[[0, 0, 255, 255], [0, 0, 255, 255], [255, 255, 0, 0], [255, 255, 0, 0]], [[255, 255, 0, 0], [255, 255, 0, 0], [0, 0, 255, 255], [0, 0, 255, 255]], [[255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0]], [[0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255]], [[255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [255, 255, 255, 255], [255, 255, 255, 255]]],
            "share2": [[[255, 255, 0, 0], [255, 255, 0, 0], [0, 0, 255, 255], [0, 0, 255, 255]], [[0, 0, 255, 255], [0, 0, 255, 255], [255, 255, 0, 0], [255, 255, 0, 0]], [[0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255]], [[255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [255, 255, 255, 255], [255, 255, 255, 255]], [[255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 0], [0, 0, 0, 0]]]
        },
        255: {
            "share1": [[[0, 0, 255, 255], [0, 0, 255, 255], [255, 255, 0, 0], [255, 255, 0, 0]], [[255, 255, 0, 0], [255, 255, 0, 0], [0, 0, 255, 255], [0, 0, 255, 255]], [[255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0]], [[0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255]], [[255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [255, 255, 255, 255], [255, 255, 255, 255]]],
            "share2": [[[0, 0, 255, 255], [0, 0, 255, 255], [255, 255, 0, 0], [255, 255, 0, 0]], [[255, 255, 0, 0], [255, 255, 0, 0], [0, 0, 255, 255], [0, 0, 255, 255]], [[255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0]], [[0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255]], [[255, 255, 255, 255], [255, 255, 255, 255], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [255, 255, 255, 255], [255, 255, 255, 255]]]
        }
    },
    "5": {
        0 : {
            "share1": [[[0, 255, 0, 255], [255, 0, 255, 0], [0, 255, 0, 255], [255, 0, 255, 0]], [[255, 0, 255, 0], [0, 255, 0, 255], [255, 0, 255, 0], [0, 255, 0, 255]], [[255, 0, 255, 0], [255, 0, 255, 0], [255, 0, 255, 0], [255, 0, 255, 0]], [[0, 255, 0, 255], [0, 255, 0, 255], [0, 255, 0, 255], [0, 255, 0, 255]], [[255, 255, 255, 255], [0, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0]], [[0, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0], [255, 255, 255, 255]]],
            "share2": [[[255, 0, 255, 0], [0, 255, 0, 255], [255, 0, 255, 0], [0, 255, 0, 255]], [[0, 255, 0, 255], [255, 0, 255, 0], [0, 255, 0, 255], [255, 0, 255, 0]], [[0, 255, 0, 255], [0, 255, 0, 255], [0, 255, 0, 255], [0, 255, 0, 255]], [[255, 0, 255, 0], [255, 0, 255, 0], [255, 0, 255, 0], [255, 0, 255, 0]], [[0, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0], [255, 255, 255, 255]], [[255, 255, 255, 255], [0, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0]]]
        },
        255: {
            "share1": [[[0, 255, 0, 255], [255, 0, 255, 0], [0, 255, 0, 255], [255, 0, 255, 0]], [[255, 0, 255, 0], [0, 255, 0, 255], [255, 0, 255, 0], [0, 255, 0, 255]], [[255, 0, 255, 0], [255, 0, 255, 0], [255, 0, 255, 0], [255, 0, 255, 0]], [[0, 255, 0, 255], [0, 255, 0, 255], [0, 255, 0, 255], [0, 255, 0, 255]], [[255, 255, 255, 255], [0, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0]], [[0, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0], [255, 255, 255, 255]]],
            "share2": [[[0, 255, 0, 255], [255, 0, 255, 0], [0, 255, 0, 255], [255, 0, 255, 0]], [[255, 0, 255, 0], [0, 255, 0, 255], [255, 0, 255, 0], [0, 255, 0, 255]], [[255, 0, 255, 0], [255, 0, 255, 0], [255, 0, 255, 0], [255, 0, 255, 0]], [[0, 255, 0, 255], [0, 255, 0, 255], [0, 255, 0, 255], [0, 255, 0, 255]], [[255, 255, 255, 255], [0, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0]], [[0, 0, 0, 0], [255, 255, 255, 255], [0, 0, 0, 0], [255, 255, 255, 255]]],
        }
    }
}

def split(img, pattern, algo="2"):
    height, width = img.shape
    w_offset = 2 if algo in ["1"] else 4
    h_offset = 4 if algo in ["4","5"] else 2
    encrypted1 = np.zeros((height * h_offset, width * w_offset), dtype=np.uint8)
    encrypted2 = np.zeros((height * h_offset, width * w_offset), dtype=np.uint8)

    for row in range(height):
        for column in range(width):
            ind = random.randint(*pattern_range[pattern])
            share1 = algo_to_pixel[algo][img[row][column]]["share1"][ind]
            share2 = algo_to_pixel[algo][img[row][column]]["share2"][ind]
            encrypted1[h_offset * row: h_offset * row + h_offset, w_offset * column: w_offset * column + w_offset] = share1
            encrypted2[h_offset * row: h_offset * row + h_offset, w_offset * column: w_offset * column + w_offset] = share2

    return encrypted1, encrypted2

def handle(file):
    file_name = input("Provide file to be shared [Default: ./secret.png] : ")
    pattern = input("\nProvide pattern to use for encryption: \n1: Diagonal\n2: Vertical\n3: Horizontal\n4: Combination of all\n")
    algo = input("\nProvide Algo to use for encryption: \n1: Shamir's\n2: Horizontal Pixel Duplication\n3: Horizontal Vector Duplication\n4: Whole Pixel Duplication\n5: Whole Vector Duplication\n")
    file = file_name if file_name else file
    img = np.asarray(Image.open(file).convert('L'))
    shares = split(img, pattern, algo)
    for index, share in enumerate(shares, 1):
        Image.fromarray(share, 'L').save(f"share[{index}].png")

if __name__ == '__main__':    
    handle("./secret.png")
