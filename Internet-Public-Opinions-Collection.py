import requests
import json

# make a GET request(XHR)
url = "https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed=20230816&geo=TW&hl=zh-TW&ns=15"
payload = {
           "hl": "zh-TW",
           "tz": "-480",
           "ed": "20230816",
           "geo": "TW",
           "hl": "zh-TW",
           "ns": "15"
           }
html = requests.get(url, data = payload)

# download datas
# typecasting：str to dict
html.encoding = "utf-8"
jsondata = json.loads(html.text)
trendingSearchesDays = jsondata["default"]["trendingSearchesDays"]
for trendingSearchesDay in trendingSearchesDays:
    news = ""
    news += "日期：" + trendingSearchesDay["formattedDate"] + "\n\n"

    for data in trendingSearchesDay["trendingSearches"]:
        news += "【主題關鍵字：" + data["title"]["query"] + "】" + "\n\n"
        
        for content in data["articles"]:
            news += "標題：" + content["title"] + "\n"
            news += "媒體：" + content["source"] + "\n"
            news += "發布時間：" + content["timeAgo"] + "\n"
            news += "內容：" + content["snippet"] + "\n"
            news += "相關連結：" + content["url"] + "\n\n"

    # store datas
    filename = trendingSearchesDay["date"] + ".txt"
    with open(filename, "w", encoding = "utf-8") as f:
        f.write(news)
    print(filename + "已存檔！")