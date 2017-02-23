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

model = HMM.unsupervised_HMM(ints_list, 18, 5)





f = open('progressions/lines_rhyming2.txt', 'w')


ints_pairs = [model.generate_sonnet_line_pair(int_to_word_map) for _ in range(7)]

def int_list_to_line(ints_list):
    words = map(lambda integer: int_to_word_map[integer], ints_pairs[0][0]) + ['\n']
    return ' '.join(words)


f.write(int_list_to_line(ints_pairs[0][0]))
f.write(int_list_to_line(ints_pairs[1][0]))
f.write(int_list_to_line(ints_pairs[0][1]))
f.write(int_list_to_line(ints_pairs[1][1]))
f.write(int_list_to_line(ints_pairs[2][0]))
f.write(int_list_to_line(ints_pairs[3][0]))
f.write(int_list_to_line(ints_pairs[2][1]))
f.write(int_list_to_line(ints_pairs[3][1]))
f.write(int_list_to_line(ints_pairs[4][0]))
f.write(int_list_to_line(ints_pairs[5][0]))
f.write(int_list_to_line(ints_pairs[4][1]))
f.write(int_list_to_line(ints_pairs[5][1]))
f.write(int_list_to_line(ints_pairs[6][0]))
f.write(int_list_to_line(ints_pairs[6][1]))



f.close()
