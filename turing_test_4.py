import numpy as np
import pandas as pd
import scipy
import csv


path = 'turing\\cardio_base.csv'

alcohol_csv_path = 'turing\\cardio_alco.csv'

cardio_csv = pd.read_csv(path)

alcohol_csv = pd.read_csv(alcohol_csv_path)


print(cardio_csv)


print(alcohol_csv)
print()

#print(cardio_csv[cardio_csv['id'] == alcohol_csv['id']])

#new_csv = pd.concat([alcohol_csv,alcohol_csv],axis=1)

#print(new_csv)

print("\n")

raw_list = np.array(alcohol_csv).reshape(-1).tolist()

print(raw_list)

print()

id_list = []
alcohol_status_list = []

for element in raw_list:


    id = element.split(";")[0]

    alcohol_status = element.split(";")[1]

    id_list.append(id)

    alcohol_status_list.append(alcohol_status)


    pass

new_dataFrame = pd.DataFrame([id_list,alcohol_status_list]).transpose()


print(new_dataFrame)

new_dataFrame.to_csv("turing\\new_alcohol.csv",index=False,index_label=None,header=['id', 'alcohol_status'])


"""csv_list = []
with open(alcohol_csv_path, 'r') as f:
    reader = csv.DictReader(f)
    for data in reader:
        csv_list.append(data)
    pass"""



