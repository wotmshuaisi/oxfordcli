import json
import sys
import os

if __name__ == "__main__":
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__) + ".."))
    sys.path.append(BASE_DIR)
    from oxford import client

    c = client.OxfordHTTPClient()

    # - word filter -
    # result = c.get_word_entries("hello")
    # with open("test.json", "w") as target:
    #     target.write(json.dumps(result))

    # - auto complete filter -
    result = c.get_auto_complete("hell")
    print(result)
