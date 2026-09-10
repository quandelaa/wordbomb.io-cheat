from wordfreq import zipf_frequency

with open("words_alpha.txt", "r", newline="") as f:
    f_reader = f.readlines()

    valid_words = []

    for row in f_reader:
        if zipf_frequency(row, "en") > 2.7:
            valid_words.append(row)

    with open("new_words.txt", "w", newline="") as f:
        for word in valid_words:
            f.write(word)
