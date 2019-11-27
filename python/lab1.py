import math
try:
    print("Enter the value of x: ")
    x = float(input())
    # positiveness = "positive" if x > 0 else "negative"
    if x > 0:
        positiveness = "positive"
    elif x == 0:
        positiveness = "zero"
    else:
        positiveness = "negative"

    print(f'x is {positiveness}')

    y = (math.cos(math.pow(x,2) + 2 * x) - x) / (math.pow(x,3) - 4 * x)
    print(f'y = {y}')
except Exception as e:
    print(e)
