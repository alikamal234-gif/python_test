temperatures = [18, 25, 31, 14, 27, 35, 22, 19, 30, 12, 28]


temperature_1 = [ i for i in temperatures if i > 25]
print(temperature_1)
temperature_2 = [i for i in temperatures if i <= 25]
print(temperature_2)
temperature_3 = [ i for i in temperatures if i <= 20 and i >= 30 ]
print(temperature_3)