import curses

def main(stdscr):
    curses.echo()
    while True:
        stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
