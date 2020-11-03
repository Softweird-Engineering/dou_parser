## DOU.UA parser bot
### Sample post
![](https://github.com/noasck/dou_parser/blob/master/sample.png)
### Requirements and libraries

- docker-compose version >= 1.25.0
- docker engine version >= 19.03.13
#### Python requirements
- psycopg2-binary==2.8.6
- SQLAlchemy==1.3.20
- pytest==6.1.1
- pyTelegramBotAPI==3.7.3
- asyncio==3.4.3
- feedparser==6.0.1
- imgkit==1.0.2
- async-timeout==3.0.1
- aiopg==1.0.0


### Environment and configuration
You need to set up **BOT_API** env to Telegram bot token in file ``` .env.bot ```. Also 
you may need to set up **ADMIN_ID** env to your chat_id with bot in the file above.
There's 2 start up options: 
- ``` docker-compose.yml ``` - main runner.
- ``` docker-compose.testbot.yml ``` - pytest runner.

### Project structure
``` 
.
├── docker-compose.testbot.yml
├── docker-compose.yml
├── env.bot
├── README.md
├── services
│   ├── parser
│   │   ├── config.py
│   │   ├── Dockerfile
│   │   ├── out.jpg
│   │   ├── parsing.info
│   │   ├── requirements.txt
│   │   ├── start.py
│   │   ├── start_test.py
│   │   └── widgets
│   │       ├── __init__.py
│   │       ├── project
│   │       │   ├── controller.py
│   │       │   ├── controller_test.py
│   │       │   ├── db.py
│   │       │   ├── db_test.py
│   │       │   ├── echo_bot.py
│   │       │   ├── __init__.py
│   │       │   └── injectors.py
│   │       └── tests
│   │           ├── fixtures.py
│   │           └── __init__.py
│   └── web
```
