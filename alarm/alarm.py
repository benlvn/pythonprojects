from playsound import playsound
import datetime
from sys import argv
#playsound('alarmsound.mp3')


if __name__ == "__main__":
    coolhour = int(argv[1])
    coolmin = int(argv[2])
    while True:
        now = datetime.datetime.now()
        if coolhour == now.hour and coolmin == now.minute:
            playsound('alarmsound.mp3')
