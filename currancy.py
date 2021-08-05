from requests import get as GET
from typing import Union
from time import localtime
from datetime import datetime
from log_config import log


class Currancy:
    __data = None
    __url_path = None
    __cc_name = None
    __last_change_date = None

    def __init__(self, cc_name: str, url_path: str):
        self.__url_path = url_path
        self.__cc_name = cc_name

    def refresh_data(self) -> Union[dict, None]:
        self.__data = self.__load_data_from_api()
        return self.__data

    def __load_data_from_api(self) -> Union[dict, None]:
        try:
            data = GET(self.__url_path).json()
        except Exception as ex:
            # TODO: logger
            log.error(f"Error[{datetime.now()}]: ")
            print(ex)
            return None
        self.__last_change_date = localtime()
        return self.__get_usd_json(data)

    @property
    def date_info(self):
        return self.__last_change_date

    def __get_usd_json(self, data: list) -> Union[dict, None]:
        return next((item for item in data if item["cc"] == self.__cc_name), None)

    @property
    def value(self) -> float:
        return self.__data["rate"]

    @property
    def date(self) -> str:
        return self.__data["exchangedate"]

    def __repr__(self) -> str:
        return str(self.__data)



