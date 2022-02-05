from create_vocab import create_vocab_set
import random


def replace_words(note, percentage, vocab):
    for line in note:
        line = line.rstrip('\n').rsplit(",")
        sentence = line[2].rsplit(" ")
        replacement_count = round((percentage * 0.01) * len(sentence))
        #replacement_words = random.choices(vocab, k=replacement_count)
        print(replacement_count)
    # print(new_note)


file_name = '/Users/alissavalentine/Charney rotation/project code/input/train_sentences_copy.txt'
f = open(file_name)
vocab_words = create_vocab_set(f)

sample_note = []
with open(file_name) as file:
    for line in file:
        line = str(line).rstrip('\n')
        sample_note.append(line)

replace_words(sample_note, 50, vocab_words)
