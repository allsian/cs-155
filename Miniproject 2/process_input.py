


f = open('project2data/shakespeare.txt', 'r')


# List of sonnets. Each sonnet is a list of words and newline chars


word_list = []

for line in f:

    line_word_list = line.split(" ")

    if line_word_list[-1][-1] == '\n':
        line_word_list[-1] = line_word_list[-1][:-1]
        line_word_list.append("\n")



    word_list.extend(line_word_list)


word_list = filter(lambda x: x != '', word_list)


sonnet_list = []
current_sonnet = []

nums = set(map(str, range(1,200)))

index = 0
while index < len(word_list):

    if word_list[index] in nums:
        sonnet_list.append(current_sonnet)
        current_sonnet = []

    else:
        current_sonnet.append(word_list[index])

    index += 1

sonnet_list = sonnet_list[1:]


for sonnet in sonnet_list:
    print sonnet
