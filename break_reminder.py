from plyer import notification
import time
# import


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = './clock.ico',
        timeout = 10,
    )


if __name__ == "__main__":
    while True:
        notifyMe("Hey User, take a break now !!", "You have worked for 20 minutes, Hey, You might have strained your eyes. Relax and close your eyes for 20 seconds")
        time.sleep(1200)
        notifyMe("Hey User, take a break now !!", "You have worked for 20 minutes, Hey, Flex some muscles. Do some stretching buddy")
        time.sleep(1200)
        notifyMe("Hey User, take a break now !!", "Hey, You have worked for 20 minutes long, Take a break")
        time.sleep(1200)