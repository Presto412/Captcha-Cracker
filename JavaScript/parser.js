const CAPCHA_DIM = [180, 45];
const CHARACTER_DIM = [30, 32];

/**
 * @function CaptchaParse
 * @param {Array} imgArray
 * The main captcha parsing algorithm,
 * requires a 2D grayscaled array of the image
 * to parse.
 */
const CaptchaParse = imgArray => {
  let captcha = "";

  const imgWidth = CAPTCHA_DIM[0];
  const imgHeight = CAPTCHA_DIM[1];

  const charWidth = CHARACTER_DIM[0];
  const charHeight = CHARACTER_DIM[1];

  const char_crop_threshold = { upper: 12 };

  for (let x = 1; x < imgHeight - 1; x++) {
    for (let y = 1; y < imgWidth - 1; y++) {
      const condition1 =
        imgArray[x][y - 1] === 255 &&
        imgArray[x][y] === 0 &&
        imgArray[x][y + 1] === 255;
      const condition2 =
        imgArray[x - 1][y] === 255 &&
        imgArray[x][y] === 0 &&
        imgArray[x + 1][y] === 255;
      const condition3 = imgArray[x][y] !== 255 && imgArray[x][y] !== 0;
      if (condition1 || condition2 || condition3) {
        imgArray[x][y] = 255;
      }
    }
  }

  for (let j = charWidth; j < imgWidth + 1; j += charWidth) {
    let matches = [];
    const chars = "123456789ABCDEFGHIJKLMNPQRSTUVWXYZ";
    for (let i = 0; i < chars.length; i++) {
      let match_count = 0;
      let black_count = 0;
      const ch = chars[i];
      const mask = bitmaps[ch];
      for (let x = 0; x < charHeight; x++) {
        for (let y = 0; y < charWidth; y++) {
          let y1 = y + j - charWidth;
          let x1 = x + char_crop_threshold[upper];
          if (imgArray[x1][y1] == mask[x][y] && mask[x][y] == 0) {
            match_count += 1;
          }
          if (mask[x][y] == 0) {
            black_count += 1;
          }
        }
      }
      const perc = match_count / black_count;
      matches.push([perc, ch]);
    }
    captcha += matches.reduce(
      (a, b) => {
        return a[0] > b[0] ? a : b;
      },
      [0, 0]
    )[1];
  }
  return captcha;
};
