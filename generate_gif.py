# script to generate a gif of the algorithm

import os
from PIL import Image

imgs = []
for img in os.listdir('saved_imgs'):
    imgs.append(Image.open('saved_imgs/'+img))

imgs[0].save('demo.gif', save_all=True, append_images=imgs[1:])