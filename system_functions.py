from os import system
from time import sleep


def bash_command(user_in):
    
    _ = system(user_in)



def clear_screen():

    bash_command('clear')


def countdown(seconds, link):
    
    # Count down until 0 so that the last second is counted
    while seconds > -1:

        mins, secs = divmod(seconds, 60)

        # Setup grammar conditions for sec/secs
        if secs != 1:
            sec_display = 'seconds'

        else:
            sec_display = 'second'

        # `timer` example: "Checking again in 1 second..."
        timer = f'{secs} {sec_display}'

        # Display the link during the countdown for quick-access
        print(f'{timer}: {link}', end="\r")

        # Wait a second
        sleep(1)

        # Take a second away from the total
        seconds -= 1

    clear_screen()


if __name__ == '__main__':

    pass
