'''
Write a script that removes blank paragraphs from HTML document. A blank paragraph
should be considered to be a <p> </p> tag containing only white spaces
'''

import argparse
import re

def main(file, out):
    html = load(file)
    cleanhtml = clean(html)
    log_result(cleanhtml)

def load(file):
    return "<html><p>ovo je jedan p</p><p>   </p><p></p></html>"

def clean(content):
    return re.sub(r'<p>[ ]*</p>', '', content)

def log_result(html, outfile):
    print(html)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='File containing the words', required=True)
    parser.add_argument('-o', '--out', help='File to write result into.', required=False)
    args = parser.parse_args()
    main(args.source, args.out)
