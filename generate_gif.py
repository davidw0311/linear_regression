# script to generate a gif of the algorithm

import os
from PIL import Image
import numpy as np
from linear_regression import run_linear_regression
import cv2

imgs = run_linear_regression()

pil_imgs = [Image.fromarray(i) for i in imgs]
pil_imgs[0].save('demo.gif', save_all=True, append_images=pil_imgs[1:])