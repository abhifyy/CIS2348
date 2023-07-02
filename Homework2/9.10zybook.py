"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""
import csv

file = input()
word_freq = {}

with open(file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        for word in row:
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1

for word, frequency in word_freq.items():
    print(word, frequency)
