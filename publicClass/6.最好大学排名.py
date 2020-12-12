import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 对返回状态抛出异常
        r.encoding = r.apparent_encoding
        print(len(r.text))
        return r.text
        # print(r.text)
    except:
        print("爬取失败")
        return ""


def fillUnitvList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr("td")
            ulist.append(
                [tds[0].text.strip(), tds[1].text.strip(), tds[4].text.strip()]
            )


def printUnivList(ulist, num):
    # 源代码
    # print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    # for i in range(num):
    #     u = ulist[i]
    #     print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))

    # 优化中文输出
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^4}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/2020"
    html = getHTMLText(url)
    fillUnitvList(uinfo, html)
    printUnivList(uinfo, 20)


if __name__ == "__main__":
    main()

