import argparse
import nltk
from create_vocab import get_fh, create_vocab_set
from create_sentences import create_s_dictionary
from create_weights import create_weights
from replace_words import replace_words
import random
import numpy


def main():
    """
    End function
    :return: 3 files: 1) synthetic notes, 2) vocab meta data, 3) sentence meta data
    """
    # Creating description and arguments for script use on the command line
    # parser = argparse.ArgumentParser(description='Give # sentences added, # notes repeated, % words replaced')
    # parser.add_argument('-s', '--sentence',
    #                     dest='s_add',
    #                     type=int,
    #                     help='# sentences added',
    #                     required=False,
    #                     default=2)
    # parser.add_argument('-n', 'note',
    #                     dest='n_repeat',
    #                     type=int,
    #                     help='# notes repeated',
    #                     required=False,
    #                     default=2)
    # parser.add_argument('-w', '--word',
    #                     dest='w_replace',
    #                     type=int,
    #                     help='% words replaced',
    #                     required=False,
    #                     default=50)
    # # parsing arguments
    # args = parser.parse_args()
    file_name = '/Users/alissavalentine/Charney rotation/project code/input/train_sentences.txt'
    train_file = get_fh(file_name, "r")
    vocab = create_vocab_set(train_file)
    sentences = create_s_dictionary(train_file)
    weights = create_weights(vocab, sentences)
    new_note, metadata = replace_words(sample_note, args.w_replace, list(vocab), weights)

    train_file.close()





if __name__ == '__main__':
    main()
