from twilio.rest import Client
from secrets import sid, token, twilio_number


client = Client(sid, token)


def twilio_call(numbers_to_call):

    for number in numbers_to_call:
    
        client.calls.create(url='http://demo.twilio.com/docs/voice.xml',
                            to=number,
                            from_=twilio_number)


def twilio_text(text_message, numbers_to_text):

    for number in numbers_to_text:

        client.messages.create(body=text_message,
                               from_=twilio_number,
                               to=number)


if __name__ == '__main__':
    
    pass
