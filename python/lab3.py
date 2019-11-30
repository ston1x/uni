def calculate_area(a,h):
    try:
        return a * h / 2
    except Exception as e:
        print(e)

def user_input():
    try:
        a = float(input("Enter a: "))
        h = float(input("Enter h: "))
    except ValueError:
        print("Something is wrong with the value, you should type int or float")
        return user_input()
    return a,h


a,h = user_input()
area = calculate_area(a,h)
print(f'Area: {area}')
