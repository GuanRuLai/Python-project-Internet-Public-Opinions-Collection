import requests
import json

# make a GET request(XHR)
url = "https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed=20230816&geo=TW&hl=zh-TW&ns=15"
payload = {
    "hl": "zh-TW",  
    "tz": "-480",
    "ed": "20230816",
    "geo": "TW",
    "ns": "15"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

try:
    html = requests.get(url, headers = headers, params = payload)
    html.raise_for_status()

    # check json
    if html.status_code == 200 and html.text:
        json_start = html.text.index('{')
        json_end = html.text.rindex('}') + 1
        json_content = html.text[json_start:json_end]

    # download datas
    # typecasting：str to dict
    jsondata = json.loads(json_content)
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
    else:
        print("No valid JSON content found in the response.")

except requests.exceptions.RequestException as e:
    print("Error:", e)
except json.JSONDecodeError as e:
    print("JSON Decode Error:", e)