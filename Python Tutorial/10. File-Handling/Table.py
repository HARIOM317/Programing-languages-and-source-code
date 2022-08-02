for i in range(2, 21):
    with open(f"Tables/Multiplication_Table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i * j}")
            if j != 10:
                f.write("\n")

print("Files have been created.")
