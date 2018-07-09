from collections import defaultdict
from string import punctuation
from heapq import nlargest
import deepcut
# import os
# import subprocess

class FrequencySummarizer:
    def __init__(self, min_cut=0.1, max_cut=0.9):
        """
         Initilize the text summarizer.
         Words that have a frequency term lower than min_cut
         or higer than max_cut will be ignored.
        """
        self._min_cut = min_cut
        self._max_cut = max_cut
        self._stopwords = None

    def construct_stopword(self):
        punctuation_list = []
        stop_word_list = []
        with open('punctuation.txt','r',encoding='utf-8')as punctuation_file:
            for row in punctuation_file:
                row = row.strip()
                punctuation_list.append(row)
        with open('stopword.txt','r',encoding='utf-8')as stopword_file:
            for row in stopword_file:
                row = row.strip()
                stop_word_list.append(row)
        self._stopwords = set(punctuation_list+stop_word_list+list(punctuation))

    def _compute_frequencies(self, word_sent):
        """
          Compute the frequency of each of word.
          Input:
           word_sent, a list of sentences already tokenized.
          Output:
           freq, a dictionary where freq[w] is the frequency of w.
        """
        self.construct_stopword()
        freq = defaultdict(int)
        for s in word_sent:
          for word in s:
            if word not in self._stopwords:
              freq[word] += 1
        # frequencies normalization and fitering
        m = float(max(freq.values()))
        for w in list(freq):
          freq[w] = freq[w]/m
          if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
            del freq[w]
        return freq

    def summarize(self, n):
        """
          Return a list of n sentences
          which represent the summary of text.
        """
        sents = []
        with open('output.txt','r',encoding='utf-8')as output:
            for row in output:
                row = row.strip()
                sents.append(row)
        # sents = sent_tokenize(text)
        assert n <= len(sents)
        word_sent = [deepcut.tokenize(s.lower()) for s in sents]
        self._freq = self._compute_frequencies(word_sent)
        ranking = defaultdict(int)
        for i,sent in enumerate(word_sent):
          for w in sent:
            if w in self._freq:
              ranking[i] += self._freq[w]
        sents_idx = self._rank(ranking, n)
        return [sents[j] for j in sents_idx]

    def _rank(self, ranking, n):
        """ return the first n sentences with highest ranking """
        return nlargest(n, ranking, key=ranking.get)

# os.system('python thai-sent_tokenize'+os.sep+'run.py')
# command = ('python thai-sent_tokenize'+os.sep+'run.py')
# subprocess.call(command)
input_path = 'input.txt'
text = ''
with open(input_path,'r',encoding='utf-8')as input_file:
    for row in input_file:
        text += row.strip()
freq = FrequencySummarizer()
with open('summerize.txt','w',encoding='utf-8')as summerize_file:
    for s in freq.summarize(2):
        summerize_file.write('*'+s+'\n')
summerize_file.close()
print('success')