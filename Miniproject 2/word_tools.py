from nltk.corpus import cmudict


pronounce_dict = cmudict.dict()


def get_number_syllables(word):

    if word in pronounce_dict:
        p = pronounce_dict[word][0]

        return len([syllable for syllable in p if syllable[-1] in '012'])

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
