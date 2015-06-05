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
import re
from itertools import groupby

def transform(word):
	#[^\w] matches all non word characters
	return (re.sub(r'[^\w]','',word)).lower()#case is ignored

def count(file):
	words = [transform(word) for word in open(file)]
	words = sorted(words)
	groupped = [(k, len(list(g))) for k, g in groupby(words)]
	filtered = [group for group in groupped if group[1] > 1]
	filtered.sort(key=lambda k: k[1], reverse=True)
	return filtered;

def log_occurence(words, outfile):

	if (outfile):
		with open(outfile, 'w') as f:
			f.writelines("{0} {1}\n".format(w[0], w[1]) for w in words)
			f.close()
			print("Output writtent to {0}".format(outfile))

	else:
		for w in words:
			print("{0} {1}".format(w[0], w[1]))
			

def main(file, out):
	words = count(file)
	log_occurence(words, out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='File containing the words.', required=True)
    parser.add_argument('-o', '--out', help='File to write result into. If not specified, console will be used.', required=False)
    args = parser.parse_args()
    main(args.source, args.out)
