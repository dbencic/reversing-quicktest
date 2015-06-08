'''
Write a script that removes blank paragraphs from HTML document. A blank paragraph
should be considered to be a <p> </p> tag containing only white spaces

paragraph cleaner
'''

import argparse
import re
import urllib.request

def load_file(file):
    with open(file) as f:
        return f.read()

def load_url(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        return str(html)

def load(source):
    if (source.startswith("http://") or source.startswith("https://")):
        return load_url(source)
    else:
        return load_file(source)

def clean(content):
    return re.sub(r'<p[^>]*>[ ]*</p>', '', content)

def log_result(html, outfile):
    if (outfile):
        with open(outfile, 'w') as f:
            f.write(html)
            print("Output writtent to {0}".format(outfile))
    else:
        print(html)

def main(source, out):
    html = load(source)
    cleanhtml = clean(html)
    log_result(cleanhtml, out)

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='File containing the html, or URL of a webpage (http:// or https://)', required=True)
    parser.add_argument('-o', '--out', help='File to write result into.', required=False)
    args = parser.parse_args()
    main(args.source, args.out)
