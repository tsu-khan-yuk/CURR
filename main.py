from tg_bot import TG_Front
from currancy import Currancy
from time import sleep, localtime
from log_config import log
from datetime import datetime as dt
from locals import *


class MyBot:
    __cc_data = None
    bot = None
    API_PATH = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

    def __init__(self) -> None:
        self.__cc_data = {
            "USD": Currancy("USD", self.API_PATH),
            "EUR": Currancy("EUR", self.API_PATH)
        }
        self.bot = TG_Front()
        self.__start_bot_engine()

    def __start_bot_engine(self):
        log.info(f"engine started [{dt.now()}]")
        time_point = False
        while True:
            if self.__refresh_cc() is True:
                log.info(f"send message [{dt.now()}]")
                self.bot.send_msg(str(self))
            while True:
                now = localtime()
                if now.tm_hour == ACTION_TIME[time_point]["H"] \
                and now.tm_min == ACTION_TIME[time_point]["M"]:
                    time_point = not time_point
                    break
                else:
                    sleep(60)

    def __refresh_cc(self) -> bool:
        for cc in self.__cc_data.values():
                if cc.refresh_data() is None:
                    return False
        return True
    
    def __repr__(self) -> str:
        string = ""
        for i in self.__cc_data.items():
            string += str(i) + "\n"
        return string


if __name__ == '__main__':
    log.info(f"system up[{dt.now()}]")
    obj = MyBot()
    # print(obj)
