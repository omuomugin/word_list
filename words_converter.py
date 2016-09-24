# -*- coding: utf-8 -*- 

def write(prefix, str) :
    file_name = './list/' + 'words_' + prefix + '.txt'
    fw = open(file_name, 'w')
    fw.write(str)
    fw.close

fr = open('words.txt', 'r')
word_prev = "a"
str = ""

for row in fr:
    word = row[0]

    if ord(word) < 97 or ord(word) > 123 :
        continue

    if not (word == word_prev) :
        write(word_prev, str)
        word_prev = word
        str = row
    else :
        str = str + row


write(word_prev, str)
fr.close