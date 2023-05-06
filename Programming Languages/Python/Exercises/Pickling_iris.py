import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
l1 = [item.split(",") for item in data.split("\n") if len(item) != 0]

with open("MyIris.pkl", "wb") as f:
    pickle.dump(l1, f)

with open("MyIris.pkl", "rb") as f:
    print(pickle.load(f))
