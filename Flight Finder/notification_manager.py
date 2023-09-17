# pip install twilio
from twilio.rest import Client


TWILIO_SID = "ACCOUNT SID"
TWILIO_AUTH_TOKEN = "AUTH TOKEN"
TWILIO_SENDER_NUMBER = "TWILIO SENDER NUMBER"
TWILIO_RECIEVER_NUMBER = "RECIEVER NUMBER"

class NotificationManager:
    def __init__(self) -> None:
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages \
            .create(
                body=message,
                from_= TWILIO_SENDER_NUMBER,
                to = TWILIO_RECIEVER_NUMBER
            )
        print(message.sid)
        