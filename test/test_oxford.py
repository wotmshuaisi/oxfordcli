import sys
import os

if __name__ == "__main__":
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__) + ".."))
    sys.path.append(BASE_DIR)
    from oxford import oxford
    from log.logger import initlogger
    initlogger()
    a = input(">")
    oxford.get_word_sense(a)
