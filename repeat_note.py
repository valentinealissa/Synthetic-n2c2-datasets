
def repeat_note(file_input):
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
                # all_notes += number * current_note
                last_id = current_id
            else:
                current_note.append(line)
    return all_notes


file_name = '/Users/alissavalentine/Charney rotation/project code/input/train_sentences.txt'
train_file = open(file_name)
new_notes = repeat_note(train_file)
