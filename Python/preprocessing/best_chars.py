import os
from PIL import Image

folder_name = "best-among-sorted"
input_folder_name = "sorted-characters"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

for _, main_dir, _ in os.walk(input_folder_name):
    for sub_dir in main_dir:
        min = 10000
        for image in os.listdir(os.path.join(input_folder_name, sub_dir)):
            img = Image.open(os.path.join(input_folder_name, sub_dir, image))
            black_count = img.getcolors()[1][0]
            if black_count < min:
                min = black_count
                img.save(os.path.join(folder_name, sub_dir + '.png'))
