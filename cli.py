#!/usr/bin/python3
import curses
from log.logger import initlogger
from oxford import oxford
import utils
import logging
import time



def main_program():
    word = []
    auto_list = []
    str_list = []
    cur_position = 0
    key = ''
    senses = ''

    utils_obj = utils.OxfordOutPutUtils(myScreen)

    myScreen.erase()
    myScreen.addstr(1, 1, '> ' + ''.join(word), curses.color_pair(1) | curses.A_BOLD)

    while key != 27:
        key = myScreen.getch(1, 3 + len(word))
        myScreen.erase()

        if key == 263 and len(word) != 0:
            #  back space
            word.pop()
        elif key >= 97 and key <= 122 or key >= 65 and key <= 90 or key == 32:
            # filter letter
            word.append(chr(key))
        elif key == 9:
            # auto complete
            auto_list = oxford.get_auto_word(''.join(word))
            utils_obj.color_add_autocomplete(auto_list)
        elif key >= 49 and key <= 54:
            # choice word
            choice = int(chr(key))
            if len(auto_list) >= choice:
                word = list(auto_list[choice - 1])
        elif key == curses.KEY_DOWN:
            # scroll able - down
            cur_position = utils_obj.scroll(
                str_list, cur_position, curses.LINES)
        elif key == curses.KEY_UP:
            # scroll able - up
            cur_position = utils_obj.scroll(
                str_list, cur_position, curses.LINES, down=False)
        elif key == 10:
            cur_position = 0
            # get senses
            senses = oxford.get_word_sense(''.join(word))
            str_list = senses.split('\n')
            utils_obj.color_add_senses(str_list)
        myScreen.addstr(1, 1, '> ' + ''.join(word), curses.color_pair(1) | curses.A_BOLD)
        myScreen.refresh()

if __name__ == '__main__':
    # init part
    initlogger()
    myScreen = curses.initscr()
    myScreen.border(0)

    curses.start_color()
    # curses.noecho()
    myScreen.keypad(1)

    utils.init_color_pair()
    # main_program
    main_program()
