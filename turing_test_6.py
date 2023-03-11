import numpy as np
import pandas as pd
import scipy


complete_csv_path = 'turing\\complete.csv'


complete_DataFrame = pd.read_csv(complete_csv_path)


#print(complete_DataFrame[complete_DataFrame['alcohol_status'] > 0])


complete_DataFrame['age'] = complete_DataFrame['age']/365

complete_DataFrame['age'] = complete_DataFrame['age'].astype('int')



print("#########################")

alcohol_population_over_fifty = len(complete_DataFrame[(complete_DataFrame['alcohol_status'] == 1) & (complete_DataFrame['age'] > 50)])

print(alcohol_population_over_fifty)

print("#########################")

fifty_years_old_population =len(complete_DataFrame[(complete_DataFrame['age'] > 50)])

print(fifty_years_old_population)

print()
print(float((alcohol_population_over_fifty/fifty_years_old_population) * 100))