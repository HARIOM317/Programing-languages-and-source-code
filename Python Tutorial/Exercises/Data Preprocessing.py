import pandas as pd

with open("iris.data") as f:
    data = f.read()
    data = data.split('\n')

# print(data)

newData = []
for line in data:
    # print(line)
    newData.append(line.split(','))

print(newData[5])
df = pd.DataFrame(newData, columns=["c1", "c2", "c3", "c4", "Type"])
# df.to_csv("mypy.csv", index=False)      # for csv file
df.to_excel("mypy.xlsx", index=False)      # for Excel file

