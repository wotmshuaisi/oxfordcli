import curses
from log.logger import initlogger
from oxford import oxford
import utils



def main_program():
    word = []
    auto_list = []
    key = ''
    senses = ''

    myScreen.erase()
    myScreen.addstr(1, 1, '> ' + ''.join(word),\
        curses.color_pair(1) | curses.A_BOLD)

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
            auto_list = oxford.get_auto_word(''.join(word))
            utils.color_add_autocomplete(auto_list, myScreen)
        elif key == 10:
            # get senses
            senses = oxford.get_word_sense(''.join(word))
            utils.color_add_senses(senses, myScreen)
        myScreen.addstr(1, 1, '> ' + ''.join(word), curses.color_pair(1) | curses.A_BOLD)
        myScreen.refresh()

if __name__ == '__main__':
    # init part
    initlogger()
    try:
        myScreen = curses.initscr()
        curses.start_color()

        utils.init_color_pair()

        main_program()
    except Exception as e:
        print(e)
    finally:
        curses.endwin()
