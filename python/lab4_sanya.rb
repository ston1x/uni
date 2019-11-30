import random

def create_matrix():
    m = int(input("Enter number of Rows"))
    n = int(input("Enter number of Columns"))
    mat = []
    for i in range(m):
        mat.append([])
    for i in range(m):
        for j in range(n):
            mat[i].append(j)
            mat[i][j] = 0

    for i in range(m):
        for j in range(n):
            print("entry in row ", i, "column", j)
            mat[i][j] = int(input())
    print(mat)
    return mat


def count_matrix_value():
    sum_matrix = 0
    count = 0
    mat = create_matrix()
    for i in mat:
        for j in i:
            sum_matrix += j
            count += 1
    print("answer is -> ", sum_matrix / count)


count_matrix_value()
