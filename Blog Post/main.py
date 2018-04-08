"""code snippets from blog post"""
import json

from PIL import Image


def main():
    """main"""

    # Opening the Image, convertring to grayscale
    image = Image.open("captcha.png").convert("L")
    pixel_matrix = image.load()
    
    # thresholding
    for column in range(0, image.height):
        for row in range(0, image.width):
            if pixel_matrix[row, column] != 0:
                pixel_matrix[row, column] = 255

    # stray line and pixel removal
    for column in range(1, image.height - 1):
        for row in range(1, image.width - 1):
            if pixel_matrix[row, column] == 0 \
                and pixel_matrix[row, column - 1] == 255 and pixel_matrix[row, column + 1] == 255:
                pixel_matrix[row, column] = 255
            if pixel_matrix[row, column] == 0 \
                and pixel_matrix[row - 1, column] == 255 and pixel_matrix[row + 1, column] == 255:
                pixel_matrix[row, column] = 255

    image.save("lessnoise_image1.png")

    # Captcha Cracking Algorithm
    characters = "123456789abcdefghijklmnpqrstuvwxyz"
    captcha = ""
    with open("bitmaps.json", "r") as fin:
        bitmap = json.load(fin)

    # parses every character, 6 is number of characters
    for j in range( int(image.width / 6), image.width + 1, int(image.width / 6)):
        char_img = image.crop((j - 30, 12, j, 44))
        char_matrix = char_img.load()
        matches = {}
        for char in characters:
            match = 0
            black = 0
            bitmap_matrix = bitmap[char]
            for col in range(0, 32):
                for row in range(0, 30):
                    if char_matrix[row, col] == bitmap_matrix[col][row] \
                        and bitmap_matrix[col][row] == 0:
                        match += 1
                    if bitmap_matrix[col][row] == 0:
                        black += 1
            perc = float(match) / float(black)
            matches.update({perc: char[0].upper()})
        try:
            captcha += matches[max(matches.keys())]
        except ValueError:
            print("failed captcha")
            captcha += "0"
    print(captcha)


if __name__ == '__main__':
    main()
