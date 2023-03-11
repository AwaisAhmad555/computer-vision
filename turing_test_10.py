import numpy as np
import pandas as pd

csv_path = 'turing\\cardio_base.csv'

dataFrame = pd.read_csv(csv_path)

#print(dataFrame)

dataFrame['age'] = dataFrame['age']/365

dataFrame['age'] = dataFrame['age'].astype('int')

print()

new_dataFrame = dataFrame['cholesterol'][dataFrame['age'] > 50]
print(new_dataFrame.value_counts())

"""
>50 = (3)6586 + 6401 = 12987

<50 = 2722 + (3)1242 = 3964

Answer = 19%
"""

print()
##############################################################


print(dataFrame['smoke'][dataFrame['gender'] == 1].value_counts())

"""

#############################

gender = 1 = male

smoker = 813 ; non-smoker = 44717 ; probability = 0.0182

gender = 2 = female

smoker = 5356 ; non-smoker = 19114 ; probability = 0.28

15 x woman more smoker



"""


print()
##############################################################

dataFrame = dataFrame.sort_values('height')

print(dataFrame['height'].iloc[69300:70000])

"""

answer = 184 cm

"""

###################

print()

print("male")
print(dataFrame['ap_hi'][dataFrame['gender'] == 1].value_counts().iloc[0:10])

print()


print("female")
print(dataFrame['ap_hi'][dataFrame['gender'] == 2].value_counts().iloc[0:10])


