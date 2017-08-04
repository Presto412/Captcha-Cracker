# VtopBetaCaptchaParser
Parses the captcha in <vtopbeta.vit.ac.in>


To use it, simply call the function in parser.py 
 Example Usage:
 ```python
 from PIL import Image
 from parser import CaptchaParse
 
 img=Image.open("IMAGE_NAME_HERE.png")
 captcha=CaptchaParse(img)
 print "CAPTCHA:"+captcha
 ```
 
 You can use the fetch.py to gather many captcha images for testing purposes.
 
 The steps.txt file is basically what was done to generate the dictionaries. The respective script names are self-explanatory. 
 
 
 
 
 Any improvements and suggestions are appreciated!Send in those PRs.
