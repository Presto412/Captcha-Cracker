import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import base64

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}


for i in tqdm(range(100)):
    response = requests.get(
        'https://vtopbeta.vit.ac.in/vtop/doRefreshCaptcha', headers=headers, verify=False)

    root = BeautifulSoup(response.text, "xml")
    img_data = root.find("img")["src"].strip("data:image/png;base64,")
    with open("download/%s.png" % i, "wb") as fh:
        fh.write(base64.b64decode(img_data))
