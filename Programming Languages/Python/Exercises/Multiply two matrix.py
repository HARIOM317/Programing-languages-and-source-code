A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[2, 4],
     [3, 2],
     [4, 3]]

C = [[0, 0],
     [0, 0],
     [0, 0]]

for i in range(len(C)):
    for j in range(len(C[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)