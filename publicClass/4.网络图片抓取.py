import requests
import os

root = "C:/Users/spy/Desktop/image/"
path = (
    "https://images-na.ssl-images-amazon.com/images/I/71-n%2B9VW%2BeL._AC_SL1500_.jpg"
)
filePath = root + path.split("/")[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(filePath):
        r = requests.get(path)
        with open(filePath, "wb") as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
