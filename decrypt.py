import numpy as np
from PIL import Image, ImageChops

def merge(share1, share2, x, y):
    share2 = ImageChops.offset(share2, int(x) if x else 0, int(y) if y else 0)
    share1, share2 = np.asarray(share1), np.asarray(share2)
    img = np.zeros(share1.shape, dtype=np.uint8)
    img[((share1 == 255) & (share2 == 255))] = 255
    return img

def handle(file1, file2):
    x = input("Provide x offset to be applied while overlapping[Default: 0]: \n")
    y = input("Provide y offset to be applied while overlapping[Default: 0]: \n")
    share1, share2 = Image.open(file1).convert('L'), Image.open(file2).convert('L')
    result = merge(share1, share2, x, y)
    Image.fromarray(result, 'L').save(f"result.png")

if __name__ == '__main__':    
    handle("./share[1].png", "./share[2].png")
