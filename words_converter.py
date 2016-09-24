# -*- coding: utf-8 -*- 

def write(prefix, str) :
    file_name = './words/' + 'words_' + prefix + '.txt'
    fw = open(file_name, 'w')
    fw.write(str)
    fw.close

fr = open('words.txt', 'r')
word_prev = ""
str = ""

for row in fr:
    word = row[0]

    if not (word == word_prev) :
        write(word_prev, str)
        word_prev = word
        str = row
    else :
        str = str + row


write(word_prev, str)