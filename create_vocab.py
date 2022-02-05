import nltk
from nltk.corpus import stopwords
import re


# Creating function to read/write file objects if file name and r or w provided
def get_fh(file_name, r_w):
    """
    :param file_name: a file name
    :param r_w: how to open a file for reading or writing ("r", or "w")
    :return: opened or closed file object
    """
    try:
        return open(file_name, r_w)
    except ValueError:  # exit script if no file name provided
        print("Error: Wrong argument was passed for the opening mode.")
        raise
    except IOError:  # exit script of no read or writing option provided
        print("Error: File cannot be opened or read.")
        raise


def create_vocab_set(file_input):
    """
    vocab generator
    :param file_input: file name
    :return: list of words to use in replacement
    """
    vocab = set()
    stop_words = set(stopwords.words('english'))
    english_words = set(nltk.corpus.words.words())
    with file_input as file:
        lines = filter(None, (line.rstrip() for line in file))
        for line in lines:
            line = str(line).rstrip('\n').rsplit(",")
            sentence = re.sub(r'[A-Za-z]{1,3}\.', '', line[2])
            word_tokens = nltk.word_tokenize(sentence)
            for w in word_tokens:
                if len(w) > 3:
                    if w not in stop_words:
                        if w in english_words:
                            vocab.add(w)
    return vocab


train_file = '/Users/alissavalentine/Charney rotation/project code/input/train_sentences.txt'
train_file = get_fh(train_file, "r")
vocab = create_vocab_set(train_file)
# train_file.close()
# vocab_file = get_fh("vocab.txt", "w")
# with vocab_file as file:
#     for word in vocab:
#         file.writelines(word)
#         file.writelines("\n")
# vocab_file.close()

