from create_vocab import create_vocab_set
from create_sentences import create_s_dictionary
from create_weights import create_weights
import random
import numpy


def replace_words(note, percentage, vocab, weight):
    seed1 = numpy.random.RandomState(40)
    seed2 = random.Random(40)
    metadata = [] # "Note #, Word #, Sentence #, Old Word, New Word"
    new_note = []
    sentence_num = 0

    ww = []
    for value in weight.values():
        ww.append(value)

    for line in note:
        line = line.rstrip('\n').rsplit(",")
        words = line[2].rsplit(" ")
        patient_id = line[0]
        challenge = line[1]

        indexed_words = []
        for word in words:
            index = words.index(word)
            indexed_word = word + "_" + str(index)
            indexed_words.append(indexed_word)

        num_2replace = round((percentage * 0.01) * len(words))

        words_2replace = seed1.choice(indexed_words, size=num_2replace, replace=False)
        #print(words_2replace)
        replacement_words = seed2.choices(vocab, k=num_2replace, weights=ww)
        #print(replacement_words)

        for count, value in enumerate(words_2replace):
            old_word = value.rsplit("_")[0]
            index = int(value.rsplit("_")[1])
            new_word = replacement_words[count]
            #print(new_word)
            words[index] = new_word
            #print(words)
            word_metadata = [patient_id, index, sentence_num, old_word, new_word]
            metadata.append(word_metadata)

        words = " ".join(words)
        new_line = str(patient_id + ',' + challenge + ',' + words)
        new_note.append(new_line)

        sentence_num += 1

    return new_note, metadata


# file_name = '/Users/alissavalentine/Charney rotation/project code/input/train_sentences_copy.txt'
# f = open(file_name)
# vocab_words = create_vocab_set(f)
# f = open(file_name)
# sentences = create_s_dictionary(f)
# weights = create_weights(vocab_words, sentences)
#
# sample_note = []
# with open(file_name) as file:
#     for line in file:
#         line = str(line).rstrip('\n')
#         sample_note.append(line)
#
# note, metadata = replace_words(sample_note, 50, list(vocab_words), weights)
#
# print(note)
# print(metadata)