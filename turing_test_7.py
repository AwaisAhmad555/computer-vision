import numpy as np
import pandas as pd


csv_path = 'turing\\covid_data.csv'

dataFrame = pd.read_csv(csv_path)

"""country = 'Spain'
country = 'Italy'
country = 'Andorra'
country = 'United States'
country = 'Belgium'"""

country = 'Italy'

population = dataFrame['population'][dataFrame['location'] == country].iloc[0].astype('int')


population_in_million = population/1000000


print('population = ',population_in_million, 'Million')

total_deaths = dataFrame['new_deaths'][dataFrame['location'] == country].sum()

print()

print('Deaths = ',total_deaths)

print()

print(total_deaths/population_in_million)


"""
                                   # Death rates
                                   
Belgium = 829.967101584729   --------  1st
Spain = 580.3898180855635    --------  2nd
Italy = 563.0494665162952    --------  3rd
United States = 338.38400089894145     --------  4th
Andorra = 51 -------  5th


"""