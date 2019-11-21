import requests
from bs4 import BeautifulSoup

import os
import time


def get_photo(url):
    try:
        headers = {'user-agent': 'Baiduspider'}
        proxies = {
            'http': 'http://122.114.31.177:808'
        }
        page = requests.get(url, headers=headers)
        # print(page.content)
        soup = BeautifulSoup(page.content, features="html.parser")
        imgs = soup.select('img')
        # imgs = soup.select('img.origin_image.zh-lightbox-thumb.lazy')
        imgs.pop(0)

        num = 0
        isExists = os.path.exists(r"D:\flaskDemo\static\photo-zhihu")
        if not isExists:
            path = os.mkdir(r"D:\flaskDemo\static\photo-zhihu")
            print("在d：创建photo-zhihu文件夹")
        for img in imgs:
            try:
                if num % 2 != 0:
                    r = requests.get(img['src'])
                    print(r.content)
                    get_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
                    with open(r"D:\flaskDemo\static\photo-zhihu\\" + get_time + str(num) + '.jpg', 'wb')as file:
                        file.write(r.content)
                        print(str(num) + 'ok')
                num = num + 1
            except Exception as e:
                print(e)

    except Exception as e:
        print(e)
        return "爬取知乎图片失败"
    return "爬取知乎图片成功"

if __name__ == "__main__":
    # get_photo("https://www.zhihu.com/question/314609358/answer/831214467")
    # get_photo("https://www.zhihu.com/question/314609358/answer/614872176")
    # get_photo("https://www.zhihu.com/question/314609358/answer/614872176")
    get_photo("https://www.zhihu.com/question/275941413/answer/745244931")