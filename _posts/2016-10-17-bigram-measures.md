---
layout: post
title: NLTK - Computing scores for Bigrams

---

[Link to source](https://github.com/samarthbhargav/samarthbhargav.github.io/tree/master/nltk-bigram-scores/compute_scores.py)

When you are working with text data, chances are you're very interested in bigrams in the data. A bigram is simply two words taken a a time.

For instance in the sentence `The quick brown fox jumps over the lazy dog`, the list of bigrams are: `(The, quick), (quick, brown), (brown, fox), (fox, jumps), (jumps, over), (over, the), (the, lazy), (lazy, dog)`. Notice that for `n` words (or tokens) in the text, you get `n-1` bigrams.

Bigrams have some interesting statistics associated with them. For instance in the whole body of text (aka corpus), how many times does `(jumps, over)` occur? How many times does `jumps` occur with other words? How many times is the second word `over`, and the first word **not** jump?

These counts tell us some important properties of the bigram. In particular, using these counts, we can compute some interesting scores, that will allow us to rank bigrams - using these ranks, we can look at 'important' bigrams.

## Loading the data
Before diving into these scores, let's use `nltk` to load up some data. I will be using the negative movie review dataset that can be found in [1](#ref-dataset). Extract the folder into "data" or the like and load it up using `PlaintextCorpusReader`:

```python
import nltk
corpus = nltk.corpus.PlaintextCorpusReader(root_folder, '.*')
# print all the file ids - you can see both the contents of "neg" and "pos" folders are loaded
print "\n".join(corpus.fileids())
print corpus.words()
```

## Cleaning up the text

We need to clean up the text. This involves removing non-alphanumeric characters and stop words (like a, an, for, etc).

First, we load up the standard English stop words that comes with `nltk` and put them into the set. You can add additional stop words as required

```python
stop_words = set(nltk.corpus.stopwords.words('english'))
```

Next let's compile a regular expression for alphanumeric characters.

```python
import re
regex = re.compile('[^a-zA-Z0-9]')
```

The following lines carries out the filtering process. Only digits are also filtered out. Note that we also convert all words to lowercase:

```python
# final list of words
all_words = []
for word in corpus.words():
    # replace non-alphabetical characters with empty string
    word = regex.sub('', word)
    # filter out
    if word == "" or word in stop_words or word.isdigit():
        continue
    all_words.append(word.lower())
```

The list `all_words` now contains the words we need.

## Computing scores

To compute a score for a given bigram $$(w_1,w_2)$$ (called a co-occurrence of $$w_1$$ and $$w_2$$), we need to know the following frequencies: $$(w_1)$$, $$(w_2)$$, $$(w_1, w_2)$$, $$(w_1, \sim w_2)$$, $$(\sim w_1, w_2)$$ and $$(\sim w_1, \sim w_2)$$. In a table format:

|                | $$w_1$$             | $$\sim w_1$$             |           |
|:-:             |:-:                  |:-:                       |:-:        |
| $$w_2$$        | $$(w_1, w_2)$$      | $$(\sim w_1, w_2)$$      | $$(w_2)$$ |
| $$\sim w_2 $$  | $$(w_1, \sim w_2)$$ | $$(\sim w_1, \sim w_2)$$ |           |
|                | $$(w_1)$$           |                          |           |

Although there are many scores we can use to rank bigrams, I'll be focusing on one score: the **Pointwise Mutual Information score (*PMI*)**. PMI can be computed by the following formula ([2](#ref-so-discussion-1), [3](#ref-wiki-pmi)):

$$
PMI\left(w_1,w_2\right) = \log\left[\frac{\left(w_1,w_2\right)N}{\left(w_1\right)\left(w_2\right)}\right]
$$

Where $$N$$ is the total number of bigrams in the data.

Good bigrams have high PMI because the probability of co-occurrence is only slightly lower than the probabilities of occurrence of each word. Conversely, a pair of words whose probabilities of occurrence are considerably higher than their probability of co-occurrence gets a small PMI score.

For computing these scores, we need to use the following classes ([4](#ref-nltk-collocations)):

- `nltk.collocations.BigramCollocationFinder`
- `nltk.collocations.BigramAssocMeasures`

To create a instance of `BigramCollocationFinder` from the words in the corpus, we can use the `from_words` class method:

```python
bigram_finder = nltk.collocations.BigramCollocationFinder.from_words(all_words)
```

The `BigramAssocMeasures` class contains frequently used scoring methods, including PMI. Although all of these are class methods, we can create a instance to avoid referring to the whole class name:

```python
bigram_measures = nltk.collocations.BigramAssocMeasures()
```

Now we can compute the PMI scores:

```python
# find the top 5 bigrams based on PMI scores:
print "Top 5 Bigrams by PMI score:", bigram_finder.nbest(bigram_measures.pmi, 5)
# to access all bigrams and their scores, use the score_ngrams method:
bigram_scores = bigram_finder.score_ngrams(bigram_measures.pmi)
print bigram_scores[0] # prints the first one - note that this is not sorted
```

## Beyond PMI

There are several other scores you can use for ranking bigrams. The full list can be found at [5](#ref-nltk-associations). For instance, for computing the Chi Square score, you can use `BigramAssocMeasures.chi_sq`:

```python
print "Top 5 Bigrams by Chi Square score:", bigram_finder.nbest(bigram_measures.chi_sq, 5)
```

## Computing scores for Trigrams

You may also need to compute the scores for trigrams: 3 words taken at a time. To do so, simple replace `BigramCollocationFinder` by `TrigramCollocationFinder` and `BigramAssocMeasures` by `BigramAssocMeasures`.

```python
trigram_finder = nltk.collocations.TrigramCollocationFinder.from_words(all_words)
trigram_measures = nltk.collocations.TrigramAssocMeasures()
print "Top 5 Trigrams by PMI score:", trigram_finder.nbest(trigram_measures.pmi, 5)
```


## References
<a name="ref-dataset"/>
1. [Movie Review Polarity Dataset](https://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz) <br/>
<a name="ref-so-discussion-1"/>
2. [Stackoverflow Discussion about PMI](http://stats.stackexchange.com/questions/80730/calculating-pointwise-mutual-information-between-two-strings) <br/>
<a name="ref-wiki-pmi"/>
3. [PMI Wiki page](https://en.wikipedia.org/wiki/Pointwise_mutual_information) <br/>
<a name="ref-nltk-collocations"/>
4. [NLTK-Collocations](http://www.nltk.org/howto/collocations.html) <br/>
<a name="ref-nltk-associations"/>
5. [NLTK-Associations](http://www.nltk.org/_modules/nltk/metrics/association.html)
