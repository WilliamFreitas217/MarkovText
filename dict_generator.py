import sys
import getopt
import glob
from markov import Markov


def check_args():
    key_length = 1
    file_list = []
    dict_file = {}

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} -k <key length> -i <input files> -d <dictionary file>")
        exit(0)
    else:
        arg = {}
        options = getopt.getopt(sys.argv[1:], 'k:i:d:')
        for item in options[0]:
            if item:
                arg[item[0]] = item[1]
        key_length = int(arg['-k'])
        dict_file = arg['-d']

        wild_card_file_list = arg['-i'].split(",")
        for file_pattern in wild_card_file_list:
            file_list += glob.glob(file_pattern)

    return key_length, file_list, dict_file


def main():
    (key_length, file_list, dict_file) = check_args()

    markov = Markov(key_length)

    for file in file_list:
        try:
            markov.read_file(file, "utf-8")
        except:
            markov.read_file(file, "windows-1252")

    markov.write_output_dict(dict_file)
    print("Generated Markov dictionary %s with processing %s input lines and %s input words " % (
        dict_file, str(markov.get_line_count()), str(markov.get_word_count())))


if __name__ == "__main__":
    main()
