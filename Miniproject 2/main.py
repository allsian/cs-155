import process_input
import baum_welch.HMM as HMM
from nltk.corpus import cmudict


pronounce_dict = cmudict.dict()


def get_number_syllables(word):
    p = pronounce_dict[word][0]
    return len([syllable for syllable in p if syllable[-1] in '012'])


print get_number_syllables('betrayal')

sonnet_list = process_input.get_sonnet_list()


word_to_int_map = {}
int_to_word_map = {}

for sonnet in sonnet_list:
    for word in sonnet:
        if word not in word_to_int_map:
            integer = len(word_to_int_map)
            word_to_int_map[word] = integer
            int_to_word_map[integer] = word

# print int_to_word_map
# print word_to_int_map

ints_list = map(lambda sonnet: map(lambda word: word_to_int_map[word], sonnet), sonnet_list)

model = HMM.unsupervised_HMM(ints_list, 18, 10)


ints_generated = model.generate_emission(120)

new_sonnet = map(lambda integer: int_to_word_map[integer], ints_generated)

print ' '.join(new_sonnet)
