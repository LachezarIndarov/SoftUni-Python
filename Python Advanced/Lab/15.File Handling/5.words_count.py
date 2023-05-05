import re


def read_words():
    with open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/words.txt', 'r') as file:
        return file.read().split(' ')


def count_words_in_file(words):
    words_counts = {
        word: 0 for word in words
    }

    with open('C:/Users/indarov/PycharmProjects/Exercise 1/Python Advanced/Lab/15.File Handling/Training/input.txt', 'r') as file:
        for line in file:
            words_in_line = [w.lower() for w in re.findall(r'\b\S+\b', line)]
            for word in words:
                words_counts[word] += words_in_line.count(word.lower())
    return words_counts


words_counts = count_words_in_file(read_words())
words_counts_sorted = sorted(words_counts.items(),
                             key=lambda x: x[1],
                             reverse=True)
[
    print(f'{w} - {c}') for w, c in words_counts_sorted
]
