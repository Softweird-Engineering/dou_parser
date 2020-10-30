## DOU.UA parser bot
### Sample post
![](https://github.com/noasck/dou_parser/sample.png)
### Requirements and libraries

- docker-compose version >= 1.25.0
- docker engine version >= 19.03.13


### Environment and configuration
You need to set up **BOT_API** env to Telegram bot token in file ``` .env.bot ```.
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
