import urllib2
import json
import sys

def get_rhymes(word):
    url = "https://api.datamuse.com/words?rel_rhy={}".format(word)
    resp = json.loads(urllib2.urlopen(url).read())
    all_words = []
    for word in resp:
        all_words += [str(word['word'])]
    return all_words

if __name__ == "__main__":
    word_to_rhyme = sys.argv[1]
    print(get_rhymes(word_to_rhyme))
