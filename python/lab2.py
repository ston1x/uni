numbers = []
try:
    while True:
        x = int(input("Enter a number: "))
        if x != 0:
            numbers.append(x)
        else:
            break
    mean = sum(numbers) / float(len(numbers))
    print(f'Mean: {mean}')
except ValueError:
    print("Something wrong with the value, you should type int or float")
except Exception as e:
    print(e)
