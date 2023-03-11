import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import least_squares


file_path = 'turing\\covid_data.csv'

cardio_dataFrame = pd.read_csv(file_path)


cardio_dataFrame['date'] = pd.to_datetime(cardio_dataFrame['date'])


#print(cardio_dataFrame[['new_cases','date']][cardio_dataFrame['location'] == 'Germany'])

date_before = datetime.datetime(2020, 3, 12)

germany_cases = cardio_dataFrame[['new_cases']][(cardio_dataFrame['location'] == 'Germany') & (cardio_dataFrame['date'] <= date_before)].sum()

print()

italy_cases = cardio_dataFrame[['new_cases']][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date']  <= date_before)].sum()

print()

print(int (italy_cases) - int (germany_cases))


print("####################################")

##########################################################


start_date = datetime.datetime(2020, 2, 28)

last_date = datetime.datetime(2020, 3, 20)


print("###########################################")



print(cardio_dataFrame[['new_cases','location','date']][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date'] >= start_date) & (cardio_dataFrame['date'] <= last_date)])

cardio_dataFrame['cumulative_cases'] = cardio_dataFrame['new_cases']

cardio_dataFrame['cumulative_cases'][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date'] >= start_date) & (cardio_dataFrame['date'] <= last_date)] = cardio_dataFrame['new_cases'][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date'] >= start_date) & (cardio_dataFrame['date'] <= last_date)].cumsum()

cardio_dataFrame['cumulative_cases'] = cardio_dataFrame['cumulative_cases'].astype('int')

print()

print(cardio_dataFrame[['new_cases','location','date','cumulative_cases']][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date'] >= start_date) & (cardio_dataFrame['date'] <= last_date)])


days_passed = cardio_dataFrame['new_cases'][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date'] >= start_date) & (cardio_dataFrame['date'] <= last_date)].index

print()

print(days_passed)


days = list (range(0,len(days_passed.tolist())))

print()

print(days)

cumulative_cases = cardio_dataFrame['cumulative_cases'][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date'] >= start_date) & (cardio_dataFrame['date'] <= last_date)]


print()
print(cumulative_cases.tolist())
#####################################################

print()

print(np.log10(cumulative_cases.tolist()))
print()
print(np.log2(cumulative_cases.tolist()))
print()
print(np.log(cumulative_cases.tolist()))

print()

unknown_constants = np.polyfit(days,np.log(cumulative_cases.tolist()),1)

print()
print(unknown_constants)

#####################################################

b = unknown_constants[0]
a = np.exp(unknown_constants[1])


print()
print(a,b)

days = [float (value) for value in days]

print()
print(days)

exponential_curve = a * np.exp(b * np.array(days))

print()

print(exponential_curve)

target_date_cases = cardio_dataFrame['cumulative_cases'][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date'] == last_date)]

print()

print()

print(int (exponential_curve[len(exponential_curve)-1]))
print()

print(int(target_date_cases))

print()


print((int (exponential_curve[len(exponential_curve)-1]))-(int(target_date_cases)))
"""
sum_cases = cardio_dataFrame['new_cases'][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date'] >= start_date) & (cardio_dataFrame['date'] <= last_date)].sum()

cases = cardio_dataFrame['new_cases'][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date'] >= start_date) & (cardio_dataFrame['date'] <= last_date)]

days_passed = cardio_dataFrame['new_cases'][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date'] >= start_date) & (cardio_dataFrame['date'] <= last_date)].index

print()
print("#######################################")
print()

print(sum_cases)


print()
print("#######################################")
print()

print(len(days_passed))

print("\n")

#cases = cardio_dataFrame['new_cases'][(cardio_dataFrame['location'] == 'Italy') & (cardio_dataFrame['date'] >= start_date) & (cardio_dataFrame['date'] <= last_date)]

#print(len(cases.tolist()))

print(cases.tolist())

print("\n")

days = list (range(0,len(days_passed.tolist())))

print()

print(pd.DataFrame([days,cases.tolist()]).transpose())

plt.plot(days,cases.tolist())
plt.plot(days,[int (a)*0.5 for a in cases.tolist()])

plt.show()

constants = np.polyfit(days,np.log(cases.tolist()),1)

print(constants)

a = constants[1]
b = constants[0]

exponential_curve = a * np.exp(b * pd.DataFrame([i for i in days]))


print()


print(exponential_curve)

"""