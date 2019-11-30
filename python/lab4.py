import numpy

def generate_from_keyboard():
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
    matrix = []
    for i in range(rows):
        matrix.append([])
    for i in range(rows):
        for j in range(columns):
            matrix[i].append(j)
            matrix[i][j] = 0

    for i in range(rows):
        for j in range(columns):
            print(f'Enter value for row {i}, column {j}: ')
            matrix[i][j] = int(input())
    print(matrix)
    return(matrix)

def generate_random_matrix():
    rows = numpy.random.randint(1,4)
    columns = numpy.random.randint(1,4)
    matrix = numpy.random.randint(10, size=(rows,columns)).tolist()
    return matrix

def build_matrix():
    if input("Do you want to enter the matrix manually? y/n: ") == "y":
        enter_by_user = True
    else:
        enter_by_user = False

    matrix = generate_from_keyboard() if enter_by_user else generate_random_matrix()
    return matrix

def divisible_by_four(matrix):
    flattened = [y for x in matrix for y in x]
    divisible_by_four = [x for x in flattened if x % 4 == 0 and x != 0]
    return divisible_by_four

try:
    matrix = build_matrix()
    divisible_by_four = divisible_by_four(matrix)
    print(f'Matrix:\n {numpy.matrix(matrix)}')
    print(f'{len(divisible_by_four)} elements can be divided by 4: {divisible_by_four}')
    # print(divisible_by_four)
except Exception as e:
    print(e)
