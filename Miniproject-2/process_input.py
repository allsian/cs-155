
import string


def get_line_list_from_file(input):

    f = open(input, 'r')


    # List of sonnets. Each sonnet is a list of words and newline chars


    word_list = []

    for line in f:

        if len(line) < 20:
            continue

        line = line.replace("-", " ")

        line_word_list = line.split(" ")

        if line_word_list[-1][-1] == '\n':
            line_word_list[-1] = line_word_list[-1][:-1]
            line_word_list.append("\n")



        word_list.extend(line_word_list)


    word_list = filter(lambda x: x != '', word_list)


    line_list = []
    current_line = []

    nums = set(map(str, range(1,200)))

    index = 0
    while index < len(word_list):

        if word_list[index] in nums or word_list[index] == "\n":
            line_list.append(current_line)
            current_line = []

        else:
            word = word_list[index]
            exclude = set(string.punctuation)
            word = ''.join(ch for ch in word if ch not in exclude)
            word = word.lower()

            current_line.append(word)

        index += 1


    line_list = filter(lambda x: len(x) > 0, line_list)
    line_list = map(lambda x: x + ['\n'], line_list)

    return line_list




def get_line_list():
    return get_line_list_from_file('project2data/shakespeare.txt') + \
            get_line_list_from_file('project2data/spenser.txt')
