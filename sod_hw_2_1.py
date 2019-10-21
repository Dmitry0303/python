from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import pandas as pd
import time



def hh_parce(base_url, headers, pages):
    # Чтобы сайт думал, что с этого браузера зашел один пользователь для просмотра вакансий
    jobs = []
    session = requests.Session()
    for i in range(pages):
        request = session.get(base_url, headers=headers)
        if request.status_code == 200:
            soup = bs(request.content, 'lxml')
            divs = soup.find_all('div', {'data-qa':'vacancy-serp__vacancy'})
            for div in divs:
                title = div.find('a', {'class': 'bloko-link HH-LinkModifier'}).text
                href = div.find('a', {'class': 'bloko-link HH-LinkModifier'})['href']
                company = div.find('a', {'data-qa':'vacancy-serp__vacancy-employer'}).text
                compensation = div.find('div', {'data-qa': 'vacancy-serp__vacancy-compensation'})
                if not compensation:
                    compensation1 = 'Нет данных'
                    compensation2 = 'Нет данных'
                else:
                    compensation = compensation.text.replace('.','')

                    if '-' in compensation:
                        compensation1 = compensation.split('-')[0]
                        compensation2 = compensation.split('-')[1]
                        #compensation2 = compensation2.replace('.','')
                        compensation1 += compensation2[-4   :]
                    elif 'от' in compensation:
                        compensation1 = compensation.replace('от ','')
                        compensation2 = 'Нет данных'
                    elif 'до' in compensation:
                        compensation1 = 'Нет данных'
                        compensation2 = compensation.replace('до ','')

                #print(compensation1, end='\t')
                #print(compensation2)
                jobs.append({
                    'title': title,
                    'href': href,
                    'company': company,
                    'compensation1': compensation1,
                    'compensation2': compensation2,
                    'source':'hh.ru'
                })
            base_url = 'https://hh.ru' + soup.find('a', {'class': 'bloko-button HH-Pager-Controls-Next HH-Pager-Control'})['href']
            time.sleep(1)
        else:
            print('Ошибка')

    jobs = pd.DataFrame(jobs)
    return jobs



def sj_parce(base_url, headers, pages):
    # Чтобы сайт думал, что с этого браузера зашел один пользователь для просмотра вакансий
    jobs = []
    session = requests.Session()
    for i in range(pages):
        request = session.get(base_url, headers=headers)
        if request.status_code == 200:
            soup = bs(request.content, 'lxml')
            divs = soup.find_all('div', {'class':'_3zucV _2GPIV f-test-vacancy-item i6-sc _3VcZr'})
            for div in divs:
                title = div.find('div', {'class': '_3mfro CuJz5 PlM3e _2JVkc _3LJqf'}).text
                href = div.find('div', {'class': '_3mfro CuJz5 PlM3e _2JVkc _3LJqf'}).findParent()['href']
                # В одном месте нет названия фирмы
                company = div.find('span', {'class': '_3mfro _3Fsn4 f-test-text-vacancy-item-company-name _9fXTd _2JVkc _3e53o _15msI'})
                if not company:
                    company = 'Нет данных'
                else:
                    company = company.getText()
                #print(company)
                compensation = div.find('span', {'class': '_3mfro _2Wp8I f-test-text-company-item-salary PlM3e _2JVkc _2VHxz'}).text
                if '—' in compensation:
                    compensation1 = compensation.split('—')[0]
                    compensation2 = compensation.split('—')[1]
                    compensation1 += compensation2[-2:]
                elif 'от' in compensation:
                    compensation1 = compensation[3:]
                    compensation2 = 'Нет данных'
                elif 'договорённости' in compensation:
                    compensation1 = compensation
                    compensation2 = compensation
                elif 'до' in compensation:
                    compensation1 = 'Нет данных'
                    compensation2 = compensation[3:]

                #print(compensation1, end='\t')
                #print(compensation2)
                #print(compensation)
                jobs.append({
                    'title': title,
                    'href': 'https://www.superjob.ru'+href,
                    'company': company,
                    'compensation1': compensation1,
                    'compensation2': compensation2,
                    'source': 'superjob.ru'
                })
            base_url = 'https://www.superjob.ru' + \
                       soup.find('a', {'class': 'icMQ_ _1_Cht _3ze9n f-test-button-dalshe f-test-link-dalshe'})['href']
            time.sleep(1)
        else:
            print('Ошибка')
    jobs = pd.DataFrame(jobs)
    return jobs

query_text = 'программист'
num_pages = 3
headers =  {'accept':'*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
base_url_hh = f'https://hh.ru/search/vacancy?area=1&search_period=3&text={query_text}'
base_url_sj = f'https://www.superjob.ru/vacancy/search/?keywords={query_text}&geo%5Bt%5D%5B0%5D=4'

jobs = hh_parce(base_url_hh, headers, num_pages)
jobs.to_csv('hh.csv')
jobs_sj = sj_parce(base_url_sj, headers, num_pages)
jobs_sj.to_csv('sj.csv')
jobs = jobs.append(jobs_sj, ignore_index=True)
jobs.to_csv('hh+sj.csv')


