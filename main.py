'''
Created on Jun 6, 2017
@author: reef425@gamil.com
'''
import curses


def main_program():
    word = []
    key = ''

    myScreen.erase()
    myScreen.addstr(1, 1, 'Word:')

    while key != 27:
        key = myScreen.getch(1, 6 + len(word))
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

        myScreen.addstr(1, 1, 'Word:' + ''.join(word))
        myScreen.refresh()


if __name__ == '__main__':
    try:
        myScreen = curses.initscr()
        main_program()
    finally:
        curses.endwin()
