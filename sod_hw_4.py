from pprint import pprint
from lxml import html
import requests
import pandas as pd
import time
import datetime

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

def mail_parce(headers):
    mail_link = ('https://www.mail.ru')

    req = requests.get(mail_link, headers=headers)
    root = html.fromstring(req.text)

    title = root.xpath('//div[@class="news-item__inner"]/a[last()]/text() | //div[@class="news-item__content"]/h3/text()')
    href = root.xpath('//div[@class="news-item__inner"]/a[last()]/@href | //div[@class="news-item o-media news-item_media news-item_main"]/a/@href')
    data_time = datetime.datetime.today()
    source_list = []

    # Переходим по ссылке каждой новости, чтобы вытянуть названия источника новости
    for link in href:
        link_req = requests.get(link, headers=headers)
        root = html.fromstring(link_req.text)
        source_name = root.xpath('//a[@class="link color_gray breadcrumbs__link"]/span/text()')
        source_list.append(source_name[0])
        time.sleep(1)

    # Формируем результат
    result = pd.DataFrame({'title' : title,
                           'href' : href,
                           'source': source_list,
                           'date_time': data_time},
                            columns=['title','href','source', 'date_time'])

    return result


result = mail_parce(headers)
pprint(result)
result.to_csv('result_mail.csv')

