import process_input
import baum_welch.HMM as HMM
import word_tools
import pickle

NUM_STATES = 50


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

# model = HMM.unsupervised_HMM(ints_list, NUM_STATES, 20)
#
# model_file = open('model_file', 'w')
#
# pickle.dump(model, model_file)
#
# model_file.close()

model_file = open('model_file', 'r')

model = pickle.load(model_file)


state_list = []
best_observations_by_state = [[] for _ in range(NUM_STATES)]

for state in range(NUM_STATES):
    print "State Number %d" % state
    generations = [(prob, int_to_word_map[i]) for i, prob in enumerate(model.O[state])]

    generations.sort(reverse=True)
    best_observations_by_state[state] = [tup[1] for tup in generations[:20]]

    meter_dict = {i : 0 for i in range(6)}

    for prob, word in generations:
        meter_dict[word_tools.classify_meter(word)] += prob

    state_list.append(meter_dict)

for idx in range(20):
    print "%s & %s & %s & %s & %s & %s \\\\" % tuple([best_observations_by_state[state][idx] for state in range(6)])

meter_to_best_state_dict = {i : 0 for i in range(6)}

for i, curr_meter_dict in enumerate(state_list):
    for meter_type in range(6):
        if curr_meter_dict[meter_type] > state_list[meter_to_best_state_dict[meter_type]][meter_type]:
            meter_to_best_state_dict[meter_type] = i


for i in range(6):
    print i, state_list[meter_to_best_state_dict[i]]


print meter_to_best_state_dict

for i in range(6):
    total = 0
    for j in range(6):
        total += model.A[meter_to_best_state_dict[i]][meter_to_best_state_dict[j]]
    for j in range(6):
        print i, j, model.A[meter_to_best_state_dict[i]][meter_to_best_state_dict[j]] / total








quit()

# {0: 0.7027706996096987, 1: 0.03880269651324091, 2: 0.009870012579427804, 3: 0.10334483759635886, 4: 0.013224526658710456, 5: 0.13198722704254212}

def generate_poem(filename):

    f = open('progressions/%s.txt' % filename, 'w')


    ints_pairs = [model.generate_sonnet_line_pair(int_to_word_map) for _ in range(7)]

    def int_list_to_line(ints_list):
        words = map(lambda integer: int_to_word_map[integer], ints_list)
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


if __name__ == '__main__':

    for i in range(0, 100):
        generate_poem('rhyming_with_line_end' + str(i))
