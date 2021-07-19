from secrets import ragdoll_link, my_number, text_to_find
from twilio_functions import twilio_call, twilio_text
import requests
from system_functions import clear_screen, countdown


def generate_startup_message(url, numbers_to_alert,
                             text_to_search):

    message = f"""URL to check:  {url}
Message on page:  {text_to_search}

A request will be sent every 60 seconds, and you will be notified when that message has changed at:
"""

    # Add all numbers to alert at the end of the message
    for number in numbers_to_alert:
        message += f'{number}\n'
    
    return message


def kitten_snipe(ragdoll_link, text_to_find,
                 numbers_to_text, numbers_to_call,
                 startup_message):

    try:

        # Display startup message on screen and text to recipients
        print(startup_message)
        twilio_text(startup_message, numbers_to_text)
        
        kitten_sniping = True
        while kitten_sniping:

            r = requests.get(ragdoll_link)
            page_text = r.text

            # If the "be patient" message is still there, try again in a minute
            if text_to_find in page_text:

                # Parameters are;  number of seconds, link to display on screen
                countdown((60 * 2), ragdoll_link)
            
            else:

                text_message_body = f"""CAT UPDATE!
    {ragdoll_link}"""

                twilio_call(numbers_to_call)
                twilio_text(text_message_body, numbers_to_text)

                kitten_sniping = False
    
    except Exception as e:

        twilio_text(f'Error!\nException: {e}\nRetrying in two minutes...', [my_number])

        countdown(60 * 2)

        kitten_snipe(ragdoll_link, text_to_find,
                     numbers_to_text, numbers_to_call,
                     startup_message)


if __name__ == '__main__':

    # Start the app with a fresh and beautiful Terminal emulator display
    clear_screen()

    # Generate a startup message and overall functionality based on secrets.py file
    message = generate_startup_message(ragdoll_link, [my_number], text_to_find)

    kitten_snipe(ragdoll_link, text_to_find, [my_number], [my_number], message)
