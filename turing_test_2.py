"""
def generateParenthesis(n, Open, close, s, temporary_list):

    if (Open == n and close == n):
        temporary_list.append(s)

    if (Open < n):
        generateParenthesis(n, Open + 1, close, s + "(",temporary_list)

    if (close < Open):
        generateParenthesis(n, Open, close + 1, s + ")", temporary_list)


    return temporary_list
    pass


def generate_combination(n):
    temporary_list = []

    combination_list = generateParenthesis(n, 0, 0, "", temporary_list)

    return combination_list
    pass


combination_number = 3

combination_list = generate_combination(n=combination_number)

print(combination_list)"""

"""import math;


def generatePowerSet(set):


    set_size = len(set)

    # set_size of power set of a set
    # with set_size n is (2**n -1)
    pow_set_size = (int)(math.pow(2, set_size))

    power_set = []

    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):


        subset = []
        for j in range(0, set_size):

            # Check if jth bit in the
            # counter is set If set then
            # print jth element from set
            
            if ((counter & (1 << j)) > 0):

                subset.append(set[j])

                pass



            pass

        power_set.append(subset)

        pass


    return power_set


# Driver program to test printPowerSet
set = [1, 2, 3]

power_set = generatePowerSet(set)


print(power_set)"""

"""import keras
from keras.layers import Dense,Input
from keras.models import Sequential


model = Sequential()

model.add(Input(shape=(10000)))
model.add(Dense(100,activation="relu"))
model.add(Dense(100,activation="relu"))


model.add(Dense(10,activation="softmax"))

print(model.summary())"""


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
####################

max_level = cardio_dataFrame["cholesterol"][cardio_dataFrame["age"] > 50].max()

print()

fifty_plus = cardio_dataFrame["cholesterol"][(cardio_dataFrame["cholesterol"] == max_level) & (cardio_dataFrame["age"] > 50)]

fifty_less = cardio_dataFrame["cholesterol"][(cardio_dataFrame["cholesterol"] == max_level) & (cardio_dataFrame["age"] < 50)]

fifty_plus = len(fifty_plus.tolist())


fifty_less = len(fifty_less.tolist())

print(fifty_plus,fifty_less)

print((fifty_less/fifty_plus) * 100)

############################

print()


man_smoker = cardio_dataFrame['id'][(cardio_dataFrame['gender'] == 1) & (cardio_dataFrame['smoke'] == 1)]

print()

woman_smoker = cardio_dataFrame['id'][(cardio_dataFrame['gender'] == 2) & (cardio_dataFrame['smoke'] == 1)]



man_non_smoker = cardio_dataFrame['id'][(cardio_dataFrame['gender'] == 1) & (cardio_dataFrame['smoke'] == 0)]

print()

woman_non_smoker = cardio_dataFrame['id'][(cardio_dataFrame['gender'] == 2) & (cardio_dataFrame['smoke'] == 0)]


print(len(man_non_smoker.tolist()), len(woman_non_smoker.tolist()))

print()

print(len(man_smoker.tolist()), len(woman_smoker.tolist()))


print((len(man_smoker.tolist()))/len(woman_smoker.tolist()))

##################################

print()


print(cardio_dataFrame['height'].max())

print(cardio_dataFrame['height'].min())

print()

print(len(cardio_dataFrame['height'][cardio_dataFrame['height'] > 191 ].tolist()))

print(len(cardio_dataFrame['height'].tolist()))

##########################

print()

import scipy.stats

x = cardio_dataFrame['ap_hi']
y = cardio_dataFrame['ap_lo']

print(scipy.stats.spearmanr(x, y))


print()

x = cardio_dataFrame['age']
y = cardio_dataFrame['weight']

print(scipy.stats.spearmanr(x, y))


print()

x = cardio_dataFrame['age']
y = cardio_dataFrame['ap_hi']

print(scipy.stats.spearmanr(x, y))


print()

x = cardio_dataFrame['gender']
y = cardio_dataFrame['height']

print(scipy.stats.spearmanr(x, y))


print()


##########################


print()

print(cardio_dataFrame['height'].mean())
print()

print(cardio_dataFrame['height'][cardio_dataFrame['height'] > 0].std())

print()

print()

#################

#alchole_dataset = pd.read_csv()






