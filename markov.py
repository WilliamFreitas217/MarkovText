import pprint
from random_generator import MLCG
import random

import nltk


class Markov(object):
    def __init__(self, order=2, dict_file="", max_word_in_sentence=20):
        self.table = {}
        self.mlcg = MLCG()
        self.input_line_count = 0
        self.input_word_count = 0
        self.order = 0
        self.max_word_in_sentence = 0
        self.set_order(order)
        self.set_max_word_in_sentence(max_word_in_sentence)
        if dict_file:
            self.load_dictionary(dict_file)

    def set_order(self, order=2):
        self.order = order

    def load_dictionary(self, dict_file):
        with open(dict_file, 'r') as inf:
            self.table = eval(inf.read())

    def read_file(self, file_name, file_encoding='utf-8'):
        with open(file_name, 'r', encoding=file_encoding) as file:
            self.process_section(' '.join(file))

    def process_section(self, line):
        sent_text = nltk.sent_tokenize(line)

        for sentence in sent_text:
            self.input_line_count = self.input_line_count + 1

            tokens = sentence.split()

            key_list = []

            self.table.setdefault('#BEGIN#', []).append(tokens[0:self.order])

            for item in tokens:
                if len(key_list) < self.order:
                    key_list.append(item)
                    continue

                self.table.setdefault(tuple(key_list), []).append(item)

                key_list.pop(0)
                key_list.append(item)
                self.input_word_count += 1

    def set_max_word_in_sentence(self, max_word_in_sentence):
        self.max_word_in_sentence = max_word_in_sentence

    def generate_text(self):
        key = int(self.mlcg.get_random_number(10, len(self.table['#BEGIN#'])))
        key = self.table['#BEGIN#'][key]
        generate_string = ' '.join(key)
        for _ in range(self.max_word_in_sentence):
            new_key = self.table.setdefault(tuple(key), '')
            if new_key == '':
                break

            new_value = random.choice(new_key)
            generate_string += ' ' + new_value

            key.pop(0)
            key.append(new_value)
        return generate_string

    def get_line_count(self):
        return self.input_line_count

    def get_word_count(self):
        return self.input_word_count

    def write_output_dict(self, file_name):
        markov_dict_file = open(file_name, 'w')
        pprint.pprint(self.table, markov_dict_file)
