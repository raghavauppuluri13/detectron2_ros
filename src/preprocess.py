import cv2
import numpy as np

def tile(img, num_tile_w, num_tile_h):
    w = img.shape[1] // num_tile_w
    h = img.shape[0] // num_tile_h
    top_lefts = [(x * h,y * w) for x in range(num_tile_h) for y in range(num_tile_w)]
    tiles = [img[x:x+h,y:y+w] for (x,y) in top_lefts]
    print([im.shape for im in tiles])
    return [img[x:x+h,y:y+w] for (x,y) in top_lefts]

def center_crop(img,min_h_per,max_h_per,min_w_per,max_w_per):
    w = img.shape[1]
    h = img.shape[0]
    new_min_h = h * min_h_per // 100 
    new_max_h = h * max_h_per // 100 
    new_max_w = w * max_w_per // 100 
    new_min_w = w * min_w_per // 100 
    img = img[new_min_h:new_max_h,new_min_w:new_max_w]
    return img

