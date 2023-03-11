######################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'turing\\cardio_base.csv'

cardio_dataFrame = pd.read_csv(file_path)


"""column_1 = cardio_dataFrame.iloc[:,1]

print(cardio_dataFrame)

new_dataFrame = pd.concat([cardio_dataFrame,column_1],axis=1)

print()

print(new_dataFrame)

x_axis = np.array([x for x in range(len(new_dataFrame['id']))])
y_axis = np.array(new_dataFrame['height'])


print()

plt.scatter(x_axis,y_axis)
plt.show()"""


cardio_dataFrame['age'] = cardio_dataFrame['age']/365

cardio_dataFrame['age'] = cardio_dataFrame['age'].astype('int')
print(cardio_dataFrame)

print()

#print(cardio_dataFrame[cardio_dataFrame['age'] > 21.0])

#print()

minimum = cardio_dataFrame['weight'].min()

print()

mean = cardio_dataFrame['weight'].mean()

print(mean)

print()

print(minimum)

print()

highest_avg_weight_grp = len(cardio_dataFrame['age'][(cardio_dataFrame['weight'] > 74) & (cardio_dataFrame['weight'] < 75)].tolist())


print(highest_avg_weight_grp)

lowest_avg_weight_grp = len(cardio_dataFrame['age'][cardio_dataFrame['weight'] == minimum].tolist())

print(lowest_avg_weight_grp)


print()

print((lowest_avg_weight_grp/highest_avg_weight_grp)*100)

print()

print((minimum/mean)*100)



