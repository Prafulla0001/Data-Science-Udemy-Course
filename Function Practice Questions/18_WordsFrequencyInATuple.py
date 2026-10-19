def count_word_frequency(sentence):
    frequency = {}

    for word in sentence.split():
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency