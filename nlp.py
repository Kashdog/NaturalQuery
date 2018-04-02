import nltk
import matplotlib as mpl
mpl.use('TkAgg')

from nltk.book import *
text1.concordance("monstrous")
text1.similar("monstrous")
print(text4)
print(100 * text4.count('a') / len(text4))
text2.common_contexts(["monstrous", "very"])
def lexical_diversity(text):
    return len(set(text)) / len(text)

print(lexical_diversity(text3))
def percentage(count, total):
    return 100 * count / total

print(percentage(text4.count('a'),len(text4)))
fdist1 = FreqDist(text1)
print(fdist1)
print(fdist1.most_common(50))
print(fdist1['whale'])
#fdist1.plot(50, cumulative=True)
V = set(text1)
long_words = [w for w in V if len(w) > 15]
print(sorted(long_words))
fdist5 = FreqDist(text5)
print(sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7]))