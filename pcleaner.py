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
        data = response.read()
        html = data.decode('utf-8')
        return html

def load(source):
    if (source.startswith("http://") or source.startswith("https://")):
        return load_url(source)
    else:
        return load_file(source)

def clean(content):
    regexpr = r'<p[^>]*>[ ]*</p>'#cleans paragraps containing only blankspaces even if <p> has attributes, but leaves paragraphs with newlines, tabs etc
    #regexpr = r'<p>[ ]*</p>'#cleans only paragraps without attributes containing only blankspaces
    #regexpr = r'<p[^>]*>[\s]*</p>'#cleans paragraps containing anny blank chars (newlines, tabs etc)
    return re.sub(regexpr, '', content)

def log_result(html, outfile):
    if (outfile):
        with open(outfile, mode='w', encoding="utf_8_sig") as f:
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
    parser.add_argument('-s', '--source', help='File containing the html, \
        or URL of a webpage (http:// or https://)', required=True)
    parser.add_argument('-o', '--out', help='File to write result into.', 
        required=False)
    args = parser.parse_args()
    main(args.source, args.out)
