import curses
from log.logger import initlogger
from oxford import oxford
import utils



def main_program():
    word = []
    key = ''
    senses = ''

    myScreen.erase()
    # myScreen.addstr(1, 1, '> '  )

    while key != 27:
        key = myScreen.getch(1, 3 + len(word))
        myScreen.erase()

        if key == 127 and len(word) != 0:
            #  back space
            word.pop()
        elif key >= 97 and key <= 122 or key >= 65 and key <= 90 or key == 32:
            # filter letter
            word.append(chr(key))
        elif key == 9:
            # auto complete
            pass
        elif key == 10:
            senses = oxford.get_word_sense(''.join(word))
            utils.color_add_str(senses, myScreen)
        myScreen.addstr(1, 1, '> ' + ''.join(word), curses.color_pair(1) | curses.A_BOLD)
        myScreen.refresh()

if __name__ == '__main__':
    initlogger()
    try:
        myScreen = curses.initscr()
        curses.start_color()

        utils.init_color_pair()

        main_program()
    finally:
        curses.endwin()
