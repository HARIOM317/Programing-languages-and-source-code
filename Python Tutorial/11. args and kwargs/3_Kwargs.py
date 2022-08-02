def function(normal, *items, **kwargs):
    print(normal)
    for item in items:
        print(item)

    print("\nNow i would like to introduce our some spacial candidates: \n")
    for key, value in kwargs.items():
        print(f"{key} is the {value}")

Items = ["Chair", "Table", "Podium", "Stage", "Mic", "Speakers", "Child water"]
Normal = "These are the items which we will have to collect eairy"
candidate = {"Hariom":"Moniter", "Abhishek":"PT Teacher", "Sonu":"Cordinator", "Pankaj":"Directer", "Sohan":"Manager"}
function(Normal, *Items, **candidate)
