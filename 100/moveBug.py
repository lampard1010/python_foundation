import re
import requests
from requests import RequestException


def get_page(url):
    try:
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        print(e)
        return None


def parse_html(html_text):
    pattern = re.compile('<li.*?list-item.*?data-title="(.*?)".*?data-score="(.*?)".*?>.*?<img.*?src="(.*?)".*?/>'
                         , re.S)
    items = re.findall(pattern, html_text)
 
    print(items)

    for item in items:
        temp_text = "'电影名称':《{0}》, '评分':{1}, '宣传海报':{2}".format(item[0], item[1], item[2])
        print(temp_text)

if __name__ == '__main__':
    url = "https://movie.douban.com/cinema/nowplaying/shanghai/"
    html_text = get_page(url)
    parse_html(html_text)