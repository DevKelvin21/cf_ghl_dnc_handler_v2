from typing import Any
import requests
import json
from .exceptions import ApiError

class VICI:
    def __init__(self, campaign: str, user: str, password: str) -> None:
        self.base_url = "http://appt.phdialer.com/vicidial/non_agent_api.php?source=CloudFunctions&campaign_id={}&user={}&pass={}".format(campaign, user, password)
        self.user = user
        self.password = password
        self.source = "CloudFunctions"

    def add_dnc(self, phone_number: str) -> Any:
        phone_number = phone_number.replace("+1", "")
        url = self.base_url + "&function=add_dnc_phone&phone_number={}".format(phone_number)
        response = requests.get(url)
        if response.status_code != 200:
            raise ApiError(response.status_code, "Failed to add DNC {}")
        return response.text