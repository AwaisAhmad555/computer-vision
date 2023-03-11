import numpy as np
import cv2 as opencv
import os
from test_split import split
import pandas as pd

#ground_truth_path = r'F:\Urdu OCR\dataset\UPTI\groundtruth'

#print(len(os.listdir(ground_truth_path)))

textlines_list = []

ground_truth_file_path = "upti_dataset_ground_truth.txt"

file1 = open(ground_truth_file_path, 'r', encoding='utf-8-sig')
Lines = file1.readlines()


print("Lines : ")
print(len(Lines))

words_list = []

for i in range(1,len(Lines)):

    """print()
    print(str(i)+" -----------")

    print(Lines[i])

    print("-----------"+ str(i))
    print()"""



    array = Lines[i].split()

    for word in array:

        for sub_word in split(word):

            words_list.append(sub_word)

            pass

        pass

pass

# removing/ pruning black spaces
new_list = []

for index, word in enumerate(words_list):

    if word != "":
        
        new_list.append(word)

        pass

    pass


#print(len(textlines_list))



final_list = list(dict.fromkeys(new_list))


ligature_list = []

for idx, ligature in enumerate(final_list):

    ligature_list.append([ligature,idx])

    pass


#print(final_list)


ligatures_DataFrame = pd.DataFrame(ligature_list,index=None,columns=None)

print(ligatures_DataFrame)

ligatures_DataFrame.to_csv("upti\\ligatures_list.csv",index=False,encoding="utf-8-sig",index_label=None)



"""

for i in range(len(os.listdir(ground_truth_path))):


    file_address = os.path.join(ground_truth_path,os.listdir(ground_truth_path)[i])



    #print(file_address)

    file1 = open(file_address, 'r', encoding='utf-8-sig')
    Lines = file1.readlines()


    #textlines_list.append(Lines)

    count = 0

    # splitting text words to non joined words





    if i == 1:

        break

        pass



    pass
    
#with open('upti_dataset_ground_truth.txt', 'w',encoding='utf-8-sig') as f:
    for line in textlines_list:
        f.writelines(line)
        #f.write('\n')
        pass
    pass
"""