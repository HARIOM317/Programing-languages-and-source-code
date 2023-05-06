m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

def matrix(m, n):
    mat = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter mat[{i}][{j}] :  "))
            row.append(inp)
        mat.append(row)
    return mat

def sum(A, B):
    output = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output



print("\nEnter matrix A\n")
A = matrix(m, n)

print("\nEnter matrix B\n")
B = matrix(m, n)

print("\nMatrix A is:")
for i in A:
    print(i)

print("\nMatrix B is:")
for i in B:
    print(i)

s = sum(A, B)
print("\nsum of matrix A and B is:")
for i in s:
    print(i)

