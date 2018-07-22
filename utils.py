import curses
import re

# keywords
word_classes = ['Noun', 'Verb', 'Adjective', 'Adverb', 'Pronoun',
    'Preposition', 'Conjunction', 'Determiner', 'Exclamation', 'Interjection']

def init_color_pair():
    # colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)


def color_add_senses(context, screen_obj):
    str_list = context.split('\n')
    context_length = len(str_list)
    for i in range(2, context_length + 2):
        # word classes
        if str_list[i - 2].strip() in word_classes:
            screen_obj.addstr(
                i + 2, 1,
                str_list[i - 2],
                curses.color_pair(1) | curses.A_BOLD | curses.A_REVERSE)
            continue
        # spelling
        if str_list[i - 2].strip().startswith('phonetic spelling'):
            screen_obj.addstr(
                i + 2, 1,
                str_list[i - 2],
                curses.color_pair(2) | curses.A_DIM)
            continue
        # short definitions
        if str_list[i - 2].strip().startswith('short definitions'):
            screen_obj.addstr(
                i + 2, 1, str_list[i - 2],
                curses.A_DIM)
            continue
        # definitions
        if str_list[i - 2].strip().startswith('definitions'):
            screen_obj.addstr(
                i + 2, 1, str_list[i - 2],
                curses.color_pair(3))
            continue
        # index
        if re.match(r'[0-9]+\.', str_list[i - 2].strip()):
            screen_obj.addstr(
                i + 2, 1, str_list[i - 2],
                curses.A_BOLD)
            continue
        screen_obj.addstr(i + 2, 1, str_list[i - 2])


def color_add_autocomplete(context, screen_obj):
    pass
