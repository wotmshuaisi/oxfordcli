from copy import deepcopy
from oxford.client import OxfordHTTPClient

oxford_client = OxfordHTTPClient()

word_desciption_format = """{type}
phonetic spelling: {ps}
senses: 
{ss}
"""

senses_format = """    {index}.
    definitions: {d}
    short definitions: {sd}
    subsenses: {sub}"""

sub_senses_format = """
        {index}.
        definitions: {d}
        short definitions: {sd}"""




def get_word_sense(word):
    o_data = oxford_client.get_word_entries(word)
    result = ""
    for word_type in o_data:
        temp_desc = deepcopy(word_desciption_format)
        temp_senses = deepcopy(senses_format)
        subsenses = ""
        for i, s in enumerate(word_type.get('senses')):
            temp_sub_senses = ""
            for ii, ss in enumerate(s.get('subsenses')):
                temp_sub_senses = deepcopy(sub_senses_format)
                temp_sub_senses = temp_sub_senses.format(
                    index=ii+1, d=', '.join(ss['definitions']), sd='; '.join(ss['short_definitions']))
                subsenses += temp_sub_senses

            temp_senses = temp_senses.format(
                index=i+1, sd=', '.join(s['short_definitions']), d='; '.join(s['definitions']), sub=subsenses)

        temp_desc = temp_desc.format(
            type=word_type['type'], ps=", ".join(word_type['phoneticSpelling']), ss=temp_senses)
        result += temp_desc
    return result
