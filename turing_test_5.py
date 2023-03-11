import numpy as np
import pandas as pd
import scipy


cardio_csv_path = "turing\\cardio_base.csv"

alcohol_csv_path = "turing\\new_alcohol.csv"

#alcohol_csv_raw_path = "turing\\cardio_alco.csv"


alcohol_dataFrame = pd.read_csv(alcohol_csv_path)

cardio_dataFrame = pd.read_csv(cardio_csv_path)

#print(alcohol_dataFrame)

print(alcohol_dataFrame)


print()
print(cardio_csv_path)

new_dataFrame = pd.merge(cardio_dataFrame,alcohol_dataFrame, on='id')

print(new_dataFrame)

new_dataFrame.to_csv("turing\\complete.csv")




####################################
#print(len(np.array(pd.read_csv(alcohol_csv_raw_path)).tolist()))

print()

print()

#ids_list = np.array(alcohol_dataFrame['id']).tolist()

#print(cardio_dataFrame)




"""for i in range(len(ids_list) - 1):


    cardio_dataFrame_index = cardio_dataFrame[cardio_dataFrame['id'] == ids_list[i]].index

    cardio_dataFrame = cardio_dataFrame.drop(cardio_dataFrame_index)


    pass

print()

print(cardio_dataFrame)"""


"""new_dataFrame = cardio_dataFrame[cardio_dataFrame['id'] == ids_list[44]]

for i in range(1,len(ids_list)-1):

    new_row_dataFrame = cardio_dataFrame[cardio_dataFrame['id'] == ids_list[i]]

    new_dataFrame = pd.concat([new_dataFrame,new_row_dataFrame],axis=0)


    pass

print(new_dataFrame)"""



"""merge_dataFrame = pd.concat([cardio_dataFrame,alcohol_dataFrame['alcohol_status']],axis=1)

merge_dataFrame = merge_dataFrame.dropna(axis=0)

merge_dataFrame = merge_dataFrame.reset_index(drop=True)


merge_dataFrame['alcohol_status'] = merge_dataFrame['alcohol_status'].astype('int')


print(merge_dataFrame)"""