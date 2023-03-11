import numpy as np
import pandas as pd
import os
import cv2 as opencv
import shutil
from test_split import split




ligatures_dataFrame_path = "upti\\ligatures_list.csv"

ligatures_dataFrame = pd.read_csv(ligatures_dataFrame_path,index_col=None,usecols=None,encoding="utf-8-sig")


folders_addresses = "upti\\upti samples"

folders_list = os.listdir(folders_addresses)

folders_list = sorted(folders_list,key=lambda a:int(a))

for folder in folders_list:

    ground_truth_path = os.path.join(folders_addresses,folder)

    files = os.listdir(ground_truth_path)

    #reading only ground truth text files (skip images)

    for file in files:

        file_extension = file.split(".")[-1]

        if file_extension == 'txt':

            text_file_path = os.path.join(ground_truth_path, file)

            text_file = open(text_file_path, 'r', encoding='utf-8-sig')
            Lines = text_file.readlines()

            ligatures_list = []

            words_list = Lines[0].split()

            # print(words_list)

            # getting words from text lines

            for word in words_list:

                #from each word extracting sub-word ligatures using custom split text program

                for sub_word in split(word):

                    ligatures_list.append(sub_word)

                    pass

                pass

            final_ligature_list = []

            #pruning empty spaces in ligature list

            for ligature in ligatures_list:

                if ligature != "":

                    final_ligature_list.append(ligature)

                    pass

                pass

            """print()

            print(final_ligature_list)
            print()
            print(file)"""

            ligature_id_list = []

            for ligature in final_ligature_list:
                """print()
                print(ligature)
                print()"""

                ligature_id = np.array(
                    ligatures_dataFrame[ligatures_dataFrame.iloc[:, 0] == ligature].iloc[:, :]).reshape(-1).tolist()

                """print(ligature_id)
                print()"""

                ligature_id_list.append(ligature_id)

                pass

            # print()
            # print(pd.DataFrame(ligature_id_list,index=None,columns=None))

            pass

        pass

    final_dataFrame = pd.DataFrame(ligature_id_list, index=None, columns=None)

    csv_file_name = ground_truth_path + "\\custom.csv"
    final_dataFrame.to_csv(csv_file_name, index=False, encoding="utf-8-sig", index_label=None)

    

    pass







word_text = "ﻣﻠﺤﻘﮧ"




####################################################################################

root_path = "upti\\upti samples"

upti_ground_truth_path = r'F:\Urdu OCR\dataset\UPTI\groundtruth'


upti_dataset_size = len(os.listdir(upti_ground_truth_path))
for i in range(1,upti_dataset_size):

    folder_path = os.path.join(root_path,str(i))

    if os.path.isdir(folder_path):

        #print(folder_path,"==>",True)

        pass
    else:

        #print(folder_path,"==>",False)

        #os.makedirs(folder_path)

        pass

    pass

upti_ground_truth_path = r'F:\Urdu OCR\dataset\UPTI\groundtruth'

upti_images_path = r'F:\Urdu OCR\dataset\UPTI\ligature_undegraded'


"""print()
print(len(os.listdir(upti_images_path)))

print()

print(len(os.listdir(root_path)))

print()

print(os.path.join(upti_images_path,os.listdir(upti_images_path)[1]))

print()

print(os.listdir(upti_images_path)[1].split(sep=".")[0])

"""
images_addresses_list = os.listdir(upti_images_path)

#print()

#print(len(images_addresses_list))

images_addresses_list = sorted(images_addresses_list,key= lambda a:int(a.split(".")[0]))

#print()
#print(images_addresses_list[21].split(".")[0])


for j in range(1,len(images_addresses_list)):

    image_name = images_addresses_list[j]

    upti_image_address = os.path.join(upti_images_path,image_name)

    

    source_path = upti_image_address
    destination_path = os.path.join(root_path,image_name.split(".")[0])+"\\"

    #shutil.copy(source_path,destination_path)


    pass



"""print("\n")
    print("----------")
    print()

    print(ground_truth_file_address)
    print()
    print(os.path.join(root_path,ground_truth_file_name.split(".")[0])+"\\")

    print()
    print("----------")
    print("\n")"""