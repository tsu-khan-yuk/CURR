import requests as req
from locals import TG_API_TOKEN, ACOUNTS_ID


class TG_Front:
    API_URL = 'https://api.telegram.org/bot' + TG_API_TOKEN + '/'

    def send_msg(self, msg: str):
        res = req.get(
            self.API_URL
            + 'sendMessage?chat_id=' + ACOUNTS_ID["self"]
            + '&text=' + msg
        )

    def get_updates(self) -> dict:
        resp = req.get(self.API_URL + "getUpdates")
        return resp.json()
