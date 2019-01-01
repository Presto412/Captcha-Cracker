# Captcha Cracker

Holds the source for the algorithm that **used to** crack the captcha at VIT University's [Academic Portal](https://vtop.vit.ac.in/vtop/). Now, they use ReCaptcha by Google.

## Related Chrome Extension

Maintained in a seperate [repository](https://github.com/Presto412/Enhancer-for-VIT-Vellore-Academics)

## Related Blog Post

Present on the [DEV](https://dev.to/presto412/how-i-cracked-the-captcha-on-my-universitys-website-237j) website.

## Running the Python Script

- Install the PIL Library(Pillow)

```bash
pip install pillow
```

- Enter the Python Directory

```bash
cd Python
```

- Run the command for the test image

```bash
python algorithm/parser.py
```

- For a performance measure, run

```bash
python performance.py
```

- For the preprocessing, run the following after deleting all folders execpt downloaded captchas

```bash
cd Python/preprocessing
python reduce-noise.py
python crop_chars.py
python character_sort.py
python best_chars.py
```

- Pick a character from the best ones as per the alphanumeric set and rename it after placing in `library-chars`.
- Run the following to generate your bitmaps

```bash
python generate_bitmaps.py
```

## License

MIT
