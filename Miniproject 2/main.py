import process_input
import baum_welch.HMM as HMM





line_list = process_input.get_line_list()


word_to_int_map = {}
int_to_word_map = {}

for line in line_list:
    for word in line:
        if word not in word_to_int_map:
            integer = len(word_to_int_map)
            word_to_int_map[word] = integer
            int_to_word_map[integer] = word

# print int_to_word_map
# print word_to_int_map

ints_list = map(lambda line: map(lambda word: word_to_int_map[word], line), line_list)

model = HMM.unsupervised_HMM(ints_list, 18, 10)


for i in range(14):
    ints_generated = model.generate_sonnet_line(int_to_word_map)

    new_sonnet = map(lambda integer: int_to_word_map[integer], ints_generated)

    print ' '.join(new_sonnet)
