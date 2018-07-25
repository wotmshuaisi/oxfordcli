import curses
import logging
import re


def init_color_pair():
    # colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

class OxfordOutPutUtils(object):

    # keywords
    word_classes = ['Noun', 'Verb', 'Adjective', 'Adverb', 'Pronoun',
        'Preposition', 'Conjunction', 'Determiner', 'Exclamation', 'Interjection']

    def __init__(self, screen_obj):
        self.screen_obj = screen_obj
        self.position = 0

    def color_add_senses(self, str_list):
        context_length = len(str_list)
        try:
            for i in range(2, context_length + 2):
                # word classes
                if str_list[i - 2].strip() in self.word_classes:
                    self.screen_obj.addstr(
                        i + 2, 1,
                        str_list[i - 2],
                        curses.color_pair(1) | curses.A_BOLD | curses.A_REVERSE)
                    continue
                # spelling
                if str_list[i - 2].strip().startswith('phonetic spelling'):
                    self.screen_obj.addstr(
                        i + 2, 1,
                        str_list[i - 2],
                        curses.color_pair(2) | curses.A_DIM)
                    continue
                # short definitions
                if str_list[i - 2].strip().startswith('short definitions'):
                    self.screen_obj.addstr(
                        i + 2, 1, str_list[i - 2],
                        curses.A_DIM)
                    continue
                # definitions
                if str_list[i - 2].strip().startswith('definitions'):
                    self.screen_obj.addstr(
                        i + 2, 1, str_list[i - 2],
                        curses.color_pair(3))
                    continue
                # index
                if re.match(r'[0-9]+\.', str_list[i - 2].strip()):
                    self.screen_obj.addstr(
                        i + 2, 1, str_list[i - 2],
                        curses.A_BOLD)
                    continue
                self.screen_obj.addstr(i + 2, 1, str_list[i - 2])
        except Exception as e:
            logging.error("utils color_add_senses {}".format(e))


    def color_add_autocomplete(self, auto_list):
        position = 0
        for i, v in enumerate(auto_list):
            temp_str = '{}.{}'.format(i+1, v)
            self.screen_obj.addstr(
                2, position, temp_str, curses.color_pair(4))
            position += len(temp_str) + 1

    def scroll(self, str_list, cur_position, line_num, down=True):
        str_list_len = len(str_list)
        logging.info("str_len %s line_num %s cur_position %s self.position %s" \
            % (str_list_len, line_num, cur_position, self.position))
        if line_num >= str_list_len:
            self.color_add_senses(str_list)
            return 0
        if cur_position > str_list_len - 1:
            # logging.info(str_list[self.position:])
            self.color_add_senses(str_list[self.position-1:])
            return self.position - 1
        if down:
            self.position = cur_position + 1
            self.color_add_senses(str_list[self.position:])
            return self.position
        if cur_position <= 0:
            self.color_add_senses(str_list[self.position:])
            return cur_position
        # logging.info(str_list[self.position:])
        self.position = cur_position - 1
        self.color_add_senses(str_list[self.position:])
        return self.position
