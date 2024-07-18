from typing import NoReturn
from twilio.rest import Client


class TwilioAPI:

    def __init__(self, account_sid: str, auth_token: str,
                 from_phone_number: str) -> None:
        self.client = Client(account_sid, auth_token)
        self.from_phone_number = from_phone_number

    def send_sms(self, message: str, to_phone_number: str) -> NoReturn:
        try:
            message = self.client.messages.create(body=message,
                                                  from_=self.from_phone_number,
                                                  to=to_phone_number)
            print("SMS sent successfully.")
        except Exception as e:
            print("Error sending SMS:", e)
