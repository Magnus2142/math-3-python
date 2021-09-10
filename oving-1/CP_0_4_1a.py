import math

results_nearly_equal_subtraction = [0] * 14
results_without_nearly_equal_subtraction = [0] * 14

x_values = [0] * 14

for i in range(0, 14):
    x_values[i] = pow(10, -(i+1))


for i in range(0, len(x_values)):
    if(x_values[i] != 0):
        results_nearly_equal_subtraction[i] = (1 - (1/math.cos(x_values[i])))/pow(math.tan(x_values[i]), 2)
        results_without_nearly_equal_subtraction[i] = -(1 / (1 + (1 / math.cos(x_values[i]))))
    

print("Results when the equation contains subtraction of nearly equal numbers: ", results_nearly_equal_subtraction)
print("\nResults when the equation does not contain subtraction of nearly equal numbers: ", results_without_nearly_equal_subtraction)





