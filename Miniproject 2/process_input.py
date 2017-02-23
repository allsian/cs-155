


f = open('project2data/shakespeare.txt', 'r')


# List of sonnets. Each sonnet is a list of words and newline chars
sonnet_list = []

word_list = []

for line in f:

    line_word_list = line.split(" ")

    if line_word_list[-1][-1] == '\n':
        line_word_list[-1] = line_word_list[-1][:-1]
        line_word_list.append("\n")



    word_list.extend(line_word_list)


word_list = filter(lambda x: x != '', word_list)

print word_list
