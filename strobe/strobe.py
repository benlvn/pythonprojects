import curses
import time
import sys

def main(stdscr):
    curses.curs_set(False)
    fps = float(sys.argv[1])
    while True:
        curses.flash()
        time.sleep(60.0/fps)

if __name__ == "__main__":
    curses.wrapper(main)
