from test_split import split
import numpy as np
import os


text_file_path = "upti\\upti samples\\1\\1.gt.txt"

text_file = open(text_file_path, 'r', encoding='utf-8-sig')

Lines = text_file.readlines()

print(Lines[0])

ligatures_list = []

final_ligature_list = []

words_list = Lines[0].split()
for word in words_list:
    for sub_word in split(word):

        ligatures_list.append(sub_word)

        pass

    pass

    final_ligature_list = []

    for ligature in ligatures_list:

        if ligature != "":

            final_ligature_list.append(ligature)

            pass

        pass


print()
print(final_ligature_list)



file = open("text_split_output.txt", "w", encoding="utf-8-sig")

file.writelines(Lines)
file.write("\n")
file.write(str(final_ligature_list))
file.close()