import statistics
import math

data = [60,61,65,63,98,99,90,95,91,96]

mean = statistics.mean(data)

deviations = []

for i in data:
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