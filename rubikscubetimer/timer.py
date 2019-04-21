import keyboard
import time

if __name__ == "__main__":
    print("Press down the a & l keys")
    while not (keyboard.is_pressed('a') and keyboard.is_pressed('l')):
        pass
    print("Let go to start the timer and solve the cube!")
    while keyboard.is_pressed('a') and keyboard.is_pressed('l'):
        pass
    start = time.time()
    print("Timing!")
    keyboard.wait('space')
    end = time.time()
    print("Great job!")
    print("Time: ", end-start)
