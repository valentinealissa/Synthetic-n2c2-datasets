import nltk


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


def create_vocab(file_input):
    """
    vocab generator
    :param file_input: file name
    :return: list of words to use in replacement
    """
    vocab = set()
    english_words = set(nltk.corpus.words.words())
    with file_input as file:
        lines = filter(None, (line.rstrip() for line in file))
        for line in lines:
            line = str(line).rstrip('\n').rsplit(",")
            sentence = line[2]
            word_tokens = nltk.word_tokenize(sentence)
            for w in word_tokens:
                if w in english_words:
                    vocab.add(w)
    return vocab


train_file = '/Users/alissavalentine/Charney rotation/project code/input/train_sentences.txt'
train_file = get_fh(train_file, "r")
vocab = create_vocab(train_file)
train_file.close()

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_more6 = 0
for word in vocab:
    if len(word) == 1:
        count_1 = count_1 + 1
    if len(word) == 2:
        count_2 = count_2 + 1
    if len(word) == 3:
        count_3 = count_3 + 1
    if len(word) == 4:
        count_4 = count_4 + 1
    if len(word) == 5:
        count_5 = count_5 + 1
    else:
        count_more6 = count_more6 + 1

print(count_1, count_2, count_3, count_4, count_5, count_more6)

