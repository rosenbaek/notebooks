from modules.textcomparer import TextComparer
import matplotlib as mpl
mpl.use("pdf")
# reset defaults because we change them further down this notebook
mpl.rcParams.update(mpl.rcParamsDefault)

import matplotlib.pyplot as plt


urls = []
urls.append("https://www.gutenberg.org/files/84/84-0.txt")
urls.append("https://www.gutenberg.org/files/1342/1342-0.txt")
urls.append("https://www.gutenberg.org/files/1260/1260-0.txt")
urls.append("https://www.gutenberg.org/files/1400/1400-0.txt")
comparer = TextComparer(urls)

comparer.multi_download()

iterable = comparer.__iter__()

print(next(iterable))
print(next(iterable))


gen = comparer.urllist_generator()
print(next(gen))
print(next(gen))


print(comparer.avg_vowels("dette er en text"))

print(comparer.hardest_read_multiprocessing())

data = comparer.hardest_read_multiprocessing()
x_values = []
y_values = []
for element in data:
    x_values.append(element[0])
    y_values.append(element[1])

plt.bar(x_values, y_values,width=0.5, align='center')
plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')
plt.ylim(min(y_values)-1, max(y_values)+1)

plt.savefig('barplot.png', bbox_inches='tight')
