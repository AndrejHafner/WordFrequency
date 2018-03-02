import matplotlib.pyplot as plt

substrings_to_replace = [";","\n",":",",","?","!",".","'"] + list(map(lambda x : str(x),range(0,10)))

def clean_words(wordlist):
    cleaned = list()
    for word in wordlist:
        for repl in substrings_to_replace:
            word = word.replace(repl,'')
        cleaned.append(word.lower())
    return list(filter(lambda x : len(x) != 0,cleaned))

def count_words(cleaned_words):
    word_count = {}
    for word in cleaned_words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    return word_count

file = open("odyssey.txt","r")
wordlist = file.read().split(" ")


cleaned_words = clean_words(wordlist)

word_count = count_words(cleaned_words)

word_count_sorted = sorted(word_count.items(), key=lambda x: x[1],reverse=True)
words_final = [word_count_sorted[idx] for idx in range(100)]

labels = [k for k,v in words_final]
values = [v for k,v in words_final]

plt.bar(range(len(values)), values, align='center')
plt.xticks(range(len(labels)), list(labels))
plt.show()



