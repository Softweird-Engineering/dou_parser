import os


class Config:
    DATABASE_URL = os.getenv('DATABASE_URL')

    PARSE_URLS = [('https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Data%20Science', 'datascience'),
                  ('https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Front%20End', 'frontend'),
                  ('https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Node.js', 'nodejs'),
                  ('https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=Python', 'python'),
                  ('https://jobs.dou.ua/vacancies/feeds/?exp=0-1&category=.NET', 'dotnet'), (
                  'https://jobs.dou.ua/vacancies/feeds/?city=%D0%9A%D0%B8%D0%B5%D0%B2&exp=0-1&category=Big%20Data',
                  'bigdata'), (
                  'https://jobs.dou.ua/vacancies/feeds/?city=%D0%9A%D0%B8%D0%B5%D0%B2&exp=0-1&category=Android',
                  'android')]

    BOT_API = os.getenv('BOT_API')
    ADMIN_ID = int(os.getenv('ADMIN_ID'))
    INIT_DB = bool(os.getenv('INIT_DB').lower() == 'true')
