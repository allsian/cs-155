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





f = open('progressions/lines_rhyming', 'w')


ints_pairs = [model.generate_sonnet_line_pair(int_to_word_map) for _ in range(7)]





new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[0][0]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[1][0]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[0][1]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[1][1]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[2][0]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[3][0]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[2][1]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[3][1]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[4][0]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[5][0]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[4][1]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[5][1]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[6][0]) + ['\n']
f.write(' '.join(new_line))

new_line = map(lambda integer: int_to_word_map[integer], ints_pairs[6][1]) + ['\n']
f.write(' '.join(new_line))




f.close()
