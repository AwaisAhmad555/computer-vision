import numpy as np
import pandas as pd

csv_path = 'turing\\covid_data.csv'

dataFrame = pd.read_csv(csv_path)

dataFrame = dataFrame.drop_duplicates(subset = ['location'])

dataFrame = dataFrame[(dataFrame['hospital_beds_per_thousand'] > 0) & (dataFrame['gdp_per_capita'] > 0) ]

dataFrame = dataFrame.iloc[:-1,:]

print()

print(dataFrame)

print()

dataFrame_1 = dataFrame[(dataFrame['hospital_beds_per_thousand'] > 5) & (dataFrame['gdp_per_capita'] > 10000) ]

print()

dataFrame_2 = dataFrame[dataFrame['hospital_beds_per_thousand'] > 5]

print()

print(len(dataFrame_1))

print()

print(len(dataFrame_2))


""" Answer : 0.88 (88%)"""
