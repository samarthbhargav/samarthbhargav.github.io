import nltk
corpus = nltk.corpus.PlaintextCorpusReader("data", '.*')
# print all the file ids - you can see both the contents of "neg" and "pos" folders are loaded
print "\n".join(corpus.fileids())
print corpus.words()

stop_words = set(nltk.corpus.stopwords.words('english'))

import re
regex = re.compile('[^a-zA-Z0-9]')

# final list of words
all_words = []
for word in corpus.words():
    # replace non-alphabetical characters with empty string
    word = regex.sub('', word)
    # filter out
    if word == "" or word in stop_words or word.isdigit():
        continue
    all_words.append(word.lower())


bigram_finder = nltk.collocations.BigramCollocationFinder.from_words(all_words)
bigram_measures = nltk.collocations.BigramAssocMeasures()

# find the top 5 bigrams based on PMI scores:
print "Top 5 Bigrams by PMI score:", bigram_finder.nbest(bigram_measures.pmi, 5)
# to access all bigrams and their scores, use the score_ngrams method:
bigram_scores = bigram_finder.score_ngrams(bigram_measures.pmi)
print bigram_scores[0] # prints the first one - note that this is not sorted

print "Top 5 Bigrams by Chi Square score:", bigram_finder.nbest(bigram_measures.chi_sq, 5)


trigram_finder = nltk.collocations.TrigramCollocationFinder.from_words(all_words)
trigram_measures = nltk.collocations.TrigramAssocMeasures()
print "Top 5 Trigrams by PMI score:", trigram_finder.nbest(trigram_measures.pmi, 5)
