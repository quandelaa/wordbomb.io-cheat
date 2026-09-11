from wordfreq import zipf_frequency

with open("tools/words_alpha.txt", "r", newline="") as f:
    f_reader = f.readlines()

    valid_words = []

    for row in f_reader:
        if zipf_frequency(row, "en") > 1.2:
            valid_words.append(row)

    with open("tools/new_words3.txt", "w", newline="") as f:
        for word in valid_words:
            f.write(word)
