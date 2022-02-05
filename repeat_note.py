from create_vocab import get_fh


def create_notes(file_input, number):
    with file_input as file:
        lines = filter(None, (line.rstrip() for line in file))
        all_notes = []
        current_note = []
        for line in lines:
            line = str(line).rstrip('\n').rsplit(",")
            current_id = line[0]
            if current_id != last_id:
                # add sentences to note here
                # replaces words in note here
                all_notes += number * current_note
                last_id = current_id
            else:
                current_note.append(line)
    return all_notes


file_name = '/Users/alissavalentine/Charney rotation/project code/input/train_sentences.txt'
train_file = get_fh(file_name, "r")
new_notes = create_notes(train_file, 3)
