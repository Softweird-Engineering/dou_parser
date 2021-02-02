"""
All models for DB here:

 --> Job
    - id
    - link : str - unique

 --> Category
    - id
    - link : str - unique

 --> Subscription
    - id
    - category_id : int - relation
    - user_id : int - relation

 --> User
    - id
    - chat_id : int - Telegram chat id - unique
"""