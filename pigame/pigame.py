import curses

if __name__ == "__main__":
    libstuff = curses.initscr()
    libstuff.beep()
    print('3.', end='')
    while True:
        num = int(input())
