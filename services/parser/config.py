import os

DATABASE_URL = os.getenv('DATABASE_URL')
PARSE_URLS = ['https://jobs.dou.ua/vacancies/feeds/?city=%D0%9A%D0%B8%D0%B5%D0%B2&exp=0-1&category=Python',
              'https://jobs.dou.ua/vacancies/feeds/?city=%D0%9A%D0%B8%D0%B5%D0%B2&exp=0-1&category=.NET',
              'https://jobs.dou.ua/vacancies/?city=%D0%9A%D0%B8%D0%B5%D0%B2&category=Data%20Science&exp=0-1']
BOT_API = os.getenv('BOT_API')
INIT_DB = bool(os.getenv('INIT_DB'))
