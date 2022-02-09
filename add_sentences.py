import random


def add_sentences(note, add_num, s_dictionary):
    meta_data = ["Note #, OG Sentence Count, New Sentence Count, "
                 "OG Note # of New Sentence, Index of New Sentence in OG Note"]
    seed2 = random.Random(40)
    og_sentence_count = len(note)
    new_sentence_count = og_sentence_count

    line = note[0].rstrip('\n').rsplit(",")
    patient_id = line[0]
    challenge = line[1]

    keys = seed2.choices(list(s_dictionary.keys()), k=add_num)
    for key in keys:
        sentence = seed2.choices(list(s_dictionary[key]), k=1)
        note.append(patient_id + "," + challenge + "," + sentence[0])
        og_note_id = key.rsplit(",")[0]
        new_sentence_count += 1
        index = list(s_dictionary[key]).index(sentence[0])
        meta_data.append([patient_id, og_sentence_count, new_sentence_count, og_note_id, index])
    return note, meta_data



