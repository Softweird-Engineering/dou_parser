from typing import TypeVar, Generic, List, Dict

Model = TypeVar('Model')


class Service(Generic[Model]):
    """
    Generic service, implements db Instance logic.
    """

    @classmethod
    async def create(cls, new_instance: Dict[str, str]) -> Model:
        """
        Creates new Instance by fields.
        :param new_instance: fields of new db record.
        :return: Model object of created record.
        """
        pass

    @classmethod
    async def get_all(cls) -> List[Model]:
        """
        Get all Instance records.
        :return: list of Model object.
        """
        pass

    @classmethod
    async def get_by_id(cls, item_id: int) -> Model:
        """
        Get Instance record with specific id.
        :param item_id: db Instance Id.
        :return: Model object.
        """
        pass

    @classmethod
    async def delete_by_id(cls, item_id: int) -> bool:
        """
        Delete Instance record from db by id.
        :param item_id: db Instance id.
        :return: True if record was successfully deleted.
        """
        pass
