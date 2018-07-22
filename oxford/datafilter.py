import json
import re
from copy import deepcopy

senses_format = {
    'definitions': '',
    'subsenses': [],
}

entries_format = {
    'type': '',
    'phoneticSpelling': [],
    'senses': [],
}


def filter_word_sense(o_data):
    # get original data
    o_data = json.loads(o_data, encoding="utf-8")
    o_data = o_data.get("results")[0]
    o_data = o_data.get("lexicalEntries")
    entries_result = []
    # filter
    for item in o_data:
        temp_entries = deepcopy(entries_format)
        temp_entries['type'] = item.get('lexicalCategory')
        temp_entries['phoneticSpelling'] = [i['phoneticSpelling'] for i in item['pronunciations']]
        
        iter_entrie = item.get('entries')
        for entrie in iter_entrie:
            for subitem in entrie['senses']:
                temp_senses = deepcopy(senses_format)
                temp_senses['definitions'] = [i for i in subitem.get('definitions')]
                temp_senses['short_definitions'] = [i for i in subitem.get('short_definitions')]
                subsenses = subitem.get('subsenses')
                if subsenses:
                    temp_senses['subsenses'] = [{'definitions': i['definitions'], 'short_definitions': i['short_definitions']} for i in subsenses]
                temp_entries['senses'].append(temp_senses)

        entries_result.append(temp_entries)
    return entries_result

def filter_auto_complete(o_data):
    result = re.findall(r'([a-zA-Z ]+)<\\\/a>', o_data)
    if len(result) > 6:
        return result[:6]
    return result
