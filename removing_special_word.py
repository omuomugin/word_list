# -*- coding: utf-8 -*- 

def write(filename, str) :
        fw = open(filename, 'w')
        fw.write(str)
        fw.close

alphabetTable = [chr(i) for i in xrange(97, 123)]

for alphabet in alphabetTable :
    file_name = './list/' + 'words_' + alphabet + '.txt'
    fr = open(file_name, 'r')

    str = ""

    for row in fr :

        if  row.find("\'") == -1 and row.find("/") == -1 :
            str = str + row

    write(file_name, str)
    fr.close