from dependency_injector import containers, providers

from .config import Config


class ConfigContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    config_factory = providers.Factory(
        Config,
        dsn=config.database.dsn,
        bot_token=config.bot.bot_token,
        admin_id=config.bot.admin_id.as_int()
    )
