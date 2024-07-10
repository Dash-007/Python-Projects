import sys
import os
from PIL import Image

# grab first and second argument
source_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through Pokedex
# convert images to png
# save to the new folder
for file in os.listdir(source_folder):
    img = Image.open(f'{source_folder}/{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}/{clean_name}.png', 'png')

print('All done!')
