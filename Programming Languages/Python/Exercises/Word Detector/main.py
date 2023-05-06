import os

def isCreature(filename):
    with open(filename, "r") as f:
        filecontent = f.read()
    if "creature" in filecontent.lower():
        return True
    else:
        return False

if __name__ == '__main__':
    # Listing the contents of this folder
    dir_contents = os.listdir()
    # for each text file, run isCreature for them
    nCreature = 0
    for item in dir_contents:
        if item.endswith("txt"):
            print(f"\nDetecting creature in {item} ")
            flag = isCreature(item)
            if(flag):
                print(f"--> --> -->Creature is present in {item} !!!!!")
                nCreature += 1
            else:
                print(f"Creature is not present in {item}")

    print("\nCreature Detector Summary!")
    print(f"{nCreature} files found with creature hidden into them.")
