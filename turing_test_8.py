import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

csv_path = 'turing\\covid_data.csv'

total_dataFrame = pd.read_csv(csv_path)

print()

new_dataFrame = total_dataFrame[['location','population','aged_65_older_percent']][total_dataFrame['aged_65_older_percent'] >= 0].drop_duplicates()

new_dataFrame['population'] = new_dataFrame['population']/1000000

print(new_dataFrame)



countries_names = new_dataFrame['location']

countries_names_list = np.array(countries_names).reshape(-1).tolist()

print()
print(countries_names_list)
print()

final_list = []

labels = []

for country in countries_names_list:

    total_deaths = total_dataFrame['new_deaths'][total_dataFrame['location'] == country].sum()

    population = float (new_dataFrame['population'][new_dataFrame['location']  == country ])

    aged_65_older_percent = int (new_dataFrame['aged_65_older_percent'][new_dataFrame['location']  == country ])
    death_rate = total_deaths / population

    if population < 0:
        death_rate = total_deaths
        pass

    print(country , ' = ' ,total_deaths ,' population = ',population, " death_rate = ", death_rate)

    final_list.append([total_deaths/population])

    if death_rate > 50.0 and aged_65_older_percent >= 20.0:
        labels.append(1)
        pass
    else:
        labels.append(0)
        pass

    pass

print()

print(new_dataFrame)

final_dataFrame = pd.DataFrame(final_list)

print()

print(final_dataFrame)

print()

print(pd.DataFrame(labels))

print()

new_dataFrame['death_rate'] = np.array(final_list).reshape(-1)

print()

X = np.array(new_dataFrame)

X = X[:,1:]
y = np.array(labels)


print(X)
print()
print(y)

print()

print(len(y[y > 0].tolist()))



"Answer = 0.15384615384615384615384615384615"




