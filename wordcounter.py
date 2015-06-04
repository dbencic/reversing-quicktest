'''
1. Write a script that takes a file containing a number of words (one per line) and sorts them
by the number of times they occur in the file (descending order), but exclude words that only
occur once. Ignore the case of the words and filter out any punctuation characters. The output
should contain lines each with word and the number of times it occurs in the input separated
by space.
Example input:
microsoft
apple
microsoft.
Apple
security
microsoft
internet
Example output:
microsoft 3
apple 2 '''

import argparse

def count(file, out):
    print((file, out))





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='File containing the words', required=True)
    parser.add_argument('-o', '--out', help='File to write result into.', default='out.txt', required=False)
    args = parser.parse_args()
    count(args.source, args.out)
