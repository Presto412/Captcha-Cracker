from PIL import Image
import os
import shutil
import json


if not os.path.exists("sorted-characters"):
    os.mkdir("sorted-characters")
else:
    shutil.rmtree('sorted-characters')
    os.mkdir("sorted-characters")


def get_similarity(img_1, img_2):
    pix1 = img_1.convert('L').load()
    pix2 = img_2.convert('L').load()
    match_count = 0
    pix1_black_count = 0
    pix2_black_count = 0

    for y in range(0, img_1.height):
        for x in range(0, img_1.width):
            if pix1[x, y] == pix2[x, y] and pix2[x, y] == 0:
                match_count += 1
            if pix2[x, y] == 0:
                pix2_black_count += 1
            if pix1[x, y] == 0:
                pix1_black_count += 1

    # no of pixels have more than 10% variation
    if float(pix1_black_count - pix2_black_count) / float(pix1_black_count + pix2_black_count) >= 1.5:
        return 0
    return float(match_count)/float(pix2_black_count)


visited_images = []
similarity_dict = {}
count = 0
for image_1_path in os.listdir("cropped-chars"):
    img_1 = Image.open(os.path.join("cropped-chars", image_1_path))
    visited_images.append(image_1_path)
    for image_2_path in os.listdir("cropped-chars"):
        if image_2_path in visited_images:
            continue
        img_2 = Image.open(os.path.join("cropped-chars", image_2_path))
        if get_similarity(img_1, img_2) >= 0.95:
            visited_images.append(image_2_path)
            if image_1_path not in similarity_dict.keys():
                count += 1
                similarity_dict[image_1_path] = [image_2_path]
                os.mkdir(os.path.join("sorted-characters", str(count)))
                img_1.save(os.path.join(
                    "sorted-characters", str(count), image_1_path))
                img_2.save(os.path.join(
                    "sorted-characters", str(count), image_2_path))
                continue
            similarity_dict[image_1_path].append(image_2_path)
            img_1.save(os.path.join(
                "sorted-characters", str(count), image_1_path))
            img_2.save(os.path.join(
                "sorted-characters", str(count), image_2_path))
