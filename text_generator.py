import getopt
import pprint
import sys

import markov


def check_args():
    max_word_in_sentence = 20
    number_of_sentences = 5

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} -w <sentence word length> -n <sentences to generate> -d <dictionary file>")
        exit(0)

    else:
        arg = {}
        options = getopt.getopt(sys.argv[1:], 'k:w:n:d:')

        for item in options[0]:
            if item:
                arg[item[0]] = item[1]

        max_word_in_sentence = int(arg['-w'])
        number_of_sentences = int(arg['-n'])
        dict_file = arg['-d']

    return max_word_in_sentence, number_of_sentences, dict_file


def main(max_word_in_sentence, dict_file, number_of_sentences=50):
    markov_obj = markov.Markov(dict_file=dict_file, max_word_in_sentence=max_word_in_sentence)

    general_text = []

    for _ in range(number_of_sentences):
        text = markov_obj.generate_text()
        print(text)
        if len(text) <= 140 and text.endswith('.'):
            general_text.append(text)

    print('\n')
    print(general_text)


if __name__ == "__main__":
    (max_n_word_sentence, sentences_qnt, file_dict) = check_args()
    main(max_n_word_sentence, file_dict, sentences_qnt)
