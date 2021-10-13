import pandas as pd
import statistics
import math

df = pd.read_csv("data.csv")
marks = df["Marks"].tolist()
#print(marks)

mean = statistics.mean(marks)

deviations = []

for i in marks:
    deviation = i - mean
    deviations.append(deviation)

squared_deviations = []

for s in deviations:
    squared_deviation = s * s
    squared_deviations.append(squared_deviation)

#print(squared_deviations)

variance = statistics.mean(squared_deviations)

standard_deviation = math.sqrt(variance)

print(standard_deviation)
