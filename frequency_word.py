sent= input("Enter a sentence: ")
word=sent.lower().split()
word_count ={}
for w in word:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print("Word Frequency:")
for w, count in word_count.items():
    print(f"{w}: {count}")