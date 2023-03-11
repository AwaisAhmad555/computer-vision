import numpy as np
import pandas as pd
import cv2 as opencv
import os
from segmentation_connected_component_labeling import connected_component_segmentation



root_path = r"C:\Users\shahzad com\PycharmProjects\urdu_ocr\upti\upti samples"


root_folders_list = os.listdir(root_path)

root_folders_list = sorted(root_folders_list,key=lambda a:int(a))


print(len(root_folders_list))

for idx,folder in enumerate(root_folders_list):

    folder_path = os.path.join(root_path,folder)

    #print(folder_path)

    files_list = os.listdir(folder_path)

    """print()

    print(files_list)

    print()"""


    for j,file in enumerate(files_list):

        file_extension = file.split(".")[-1]

        if file_extension == "csv":

            csv_file_path = os.path.join(folder_path,file)

            try:

                ligatures_dataFrame = pd.read_csv(csv_file_path, index_col=None)

                ligatures_id_list = np.array(ligatures_dataFrame.iloc[:, 1]).tolist()

                pass
            except:

                ligatures_id_list = []
                print("error in reading csv !")

                pass





            """print()
            print(ligatures_id_list)
            print()"""


            pass

        if file_extension == 'png':

            image_path = os.path.join(folder_path,file)

            image = opencv.imread(image_path)

            #opencv.imshow("image",image)

            segment_images_list = connected_component_segmentation(img=image)

            for id,segment_image in enumerate(segment_images_list):

                #opencv.imshow(""+str(id),segment_image)

                pass

            pass

        if j == len(files_list)-1:

            """print()
            print("segment images list size : ")
            print(len(segment_images_list))

            print()

            print("ligature id list size : ")
            print(len(ligatures_id_list))"""

            segment_images_list_size = len(segment_images_list)
            ligatures_id_list_size = len(ligatures_id_list)

            if segment_images_list_size == ligatures_id_list_size:

                training_dataset_path = "upti\\upti_extracted_images\\"


                for image_id,image in zip(ligatures_id_list,segment_images_list):

                    image_folder_path = training_dataset_path + str(image_id)

                    if os.path.isdir(image_folder_path):
                        pass
                    else:
                        os.makedirs(image_folder_path)
                        pass

                    image_name = len(os.listdir(image_folder_path))

                    complete_path = image_folder_path + "\\" + str(image_name) + ".png"

                    opencv.imwrite(complete_path,image)

                    pass


                pass


            pass


        pass

    """if idx == 1:

        break

        pass"""


    pass


opencv.waitKey(0)
opencv.destroyAllWindows()