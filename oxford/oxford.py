from copy import deepcopy
from oxford.client import OxfordHTTPClient
import logging

oxford_client = OxfordHTTPClient()

word_desciption_format = """{type}
phonetic spelling: {ps}
senses: 
{ss}"""

senses_format = """    {index}.
    definitions: {d}
    short definitions: {sd}
    examples: {exp}
    subsenses: {sub}
"""

sub_senses_format = """
        {index}.
        definitions: {d}
        short definitions: {sd}
"""


def get_word_sense(word):
    o_data = oxford_client.get_word_entries(word)
    result = ""
    for word_type in o_data:

        temp_desc = ""
        temp_senses = ""

        for i, s in enumerate(word_type.get('senses')):
            subsenses = ""
            for ii, ss in enumerate(s.get('subsenses')):
                temp_sub_senses = sub_senses_format.format(
                    index=ii+1, d=', '.join(ss['definitions']), sd='; '.join(ss['short_definitions']))
                subsenses += temp_sub_senses

            temp_senses += senses_format.format(
                index=i+1, sd=', '.join(
                    s['short_definitions']),
                    d='; '.join(s['definitions']),
                    exp='; '.join(s['examples']),
                    sub=subsenses)

        temp_desc = word_desciption_format.format(
            type=word_type['type'], ps=", ".join(word_type['phoneticSpelling']), ss=temp_senses)
        result += temp_desc
    return result


def get_auto_word(word_part):
    return oxford_client.get_auto_complete(word_part)
