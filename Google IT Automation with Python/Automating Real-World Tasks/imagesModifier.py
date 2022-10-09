#!/usr/bin/env python3
import os
from PIL import Image

cwd = os.getcwd()
path = cwd + '/images/'
new_path = '/opt/icons/'

if not os.path.exists(new_path):
    os.makedirs(new_path)

for file in os.listdir(path):
    if not file.startswith('.'):
        im = Image.open(path + file)
        im.convert('RGB').rotate(270).resize((128,128)).save(new_path + file, 'JPEG')
        im.close()