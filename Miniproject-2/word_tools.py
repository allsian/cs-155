from nltk.corpus import cmudict


pronounce_dict = cmudict.dict()


def get_number_syllables(word):

    if word in pronounce_dict:
        p = pronounce_dict[word][0]

        return get_number_syllables_in_pronunciation(p)

    else:
        count = 0

        in_vowel_cluster = False

        for char in word:
            if char in 'aeiouy' and not in_vowel_cluster:
                in_vowel_cluster = True
                count += 1

            elif char not in 'aeiouy':
                in_vowel_cluster = False

        return count

def get_number_syllables_in_pronunciation(pronunciation):
    return len([phoneme for phoneme in pronunciation if phoneme[-1] in '012'])




def rhymes_with(word1, word2):

    if word1 == word2:
        return False

    if word1 not in pronounce_dict or word2 not in pronounce_dict:
        return False

    return any(rhyming_pronunciations(p1, p2) for p1 in pronounce_dict[word1] for p2 in pronounce_dict[word2])

def rhyming_pronunciations(phoneme_list1, phoneme_list2):

    # print phoneme_list1, phoneme_list2

    index = -1

    vowels1 = [phoneme[:-1] for phoneme in phoneme_list1 if phoneme[-1] in '012']
    vowels2 = [phoneme[:-1] for phoneme in phoneme_list2 if phoneme[-1] in '012']

    if len(vowels1) >= 2 and len(vowels2) >= 2:
        if vowels1[-2] != vowels2[-2]:
            return False

    while True:
        if phoneme_list1[index][-1] not in '012':
            if phoneme_list1[index] != phoneme_list2[index]:
                return False

            index -= 1

        else:
            return phoneme_list1[index][:-1] == phoneme_list2[index][:-1]



assert rhymes_with("boy", "toy")
assert rhymes_with("boat", "float")
assert rhymes_with("eyes", "dies")
assert rhymes_with("painted", "acquainted")
assert not rhymes_with("rolling", "falling")
assert rhymes_with("rolling", "controlling")
assert rhymes_with("say", "decay")
assert rhymes_with("quality", "astronomy")
assert rhymes_with("abuse", "use")
assert rhymes_with("husbandry", "posterity")
assert rhymes_with("quality", "astronomy")


ONE_SYLLABLE = 0
EVEN_SYLLABLE_IAMB = 1
ODD_SYLLABLE_IAMB = 2
EVEN_SYLLABLE_TROCHEE = 3
ODD_SYLLABLE_TROCHEE = 4
UNIDENTIFIED = 5

def classify_meter(word):

    num_syllables = get_number_syllables(word)

    if num_syllables == 1:
        return ONE_SYLLABLE

    elif num_syllables % 2 == 0:

        if word in pronounce_dict:
            pronunciation = pronounce_dict[word][0]

            vowels = [phoneme for phoneme in pronunciation if phoneme[-1] in '012']

            emphases = [int(v[-1]) for v in vowels]

            if emphases[0] == 0:
                return EVEN_SYLLABLE_IAMB
            if emphases[0] >= 1:
                return EVEN_SYLLABLE_TROCHEE

    elif num_syllables % 2 == 1:

        if word in pronounce_dict:
            pronunciation = pronounce_dict[word][0]

            vowels = [phoneme for phoneme in pronunciation if phoneme[-1] in '012']

            emphases = [int(v[-1]) for v in vowels]

            if emphases[0] == 0:
                return ODD_SYLLABLE_IAMB
            if emphases[0] >= 1:
                return ODD_SYLLABLE_TROCHEE
    return UNIDENTIFIED


assert classify_meter("hello") == EVEN_SYLLABLE_IAMB
assert classify_meter("ape") == ONE_SYLLABLE
assert classify_meter("mouse") == ONE_SYLLABLE
assert classify_meter("estuary") == EVEN_SYLLABLE_TROCHEE
assert classify_meter("estuary") == EVEN_SYLLABLE_TROCHEE
assert classify_meter("situate") == ODD_SYLLABLE_TROCHEE
assert classify_meter("tidal") == EVEN_SYLLABLE_TROCHEE
assert classify_meter("distract") == EVEN_SYLLABLE_IAMB
assert classify_meter("distracted") == ODD_SYLLABLE_IAMB
assert classify_meter("\n") == UNIDENTIFIED
#assert classify_meter("contracted") == ODD_SYLLABLE_IAMB
