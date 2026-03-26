def word_frequency_calculator(text):
    word_freq={}
    words=text.split()
    for word in words:
        word=word.lower()
        word=word.strip('.,!?";()')
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

text=input("Enter a string: ")
frequencies=word_frequency_calculator(text)
print("Word Frequencies:")
for word, freq in frequencies:
    print(f"{word}: {freq}")