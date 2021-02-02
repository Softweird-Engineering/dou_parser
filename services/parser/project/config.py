import re
import logging

logger = logging.getLogger('DOU_JOBS Parser-2.0')


class Config:
    """
    Configuration store class.
    """
    def __init__(self, dsn: str, bot_token: str, admin_id: int):
        """
        Constructor of configuration
        :param dsn: database server name
        :param bot_token: Telegram Bot API Token
        :param admin_id: admin chat Telegram API
        """
        pattern = r"postgresql://[\w_]+:[\w_]+@db:5432/[\w]+"
        if not re.match(pattern, dsn):
            logger.error("DSN, supplied in configuration is invalid.")
            raise ValueError("DSN is invalid")

        if not isinstance(admin_id, int):
            logger.error("Admin chat Id is invalid.")
            raise ValueError("Admin chat Id is invalid.")

        self.dsn = dsn
        self.bot_token = bot_token
        self.admin_id = admin_id
