class Employee:
    no_of_leaves = 12
    Working_time = 8
    no_of_stocks = 5

    @classmethod
    def change_policy(cls, new_leaves, new_time):
        cls.no_of_leaves = new_leaves
        cls.Working_time = new_time

Hariom = Employee()
Ansh = Employee()
print("No. of leaves = ", Ansh.no_of_leaves)
print("Woking time = ", Ansh.Working_time)
Hariom.change_policy(15, 6)
print("No. of leaves = ", Ansh.no_of_leaves)
print("Woking time = ", Ansh.Working_time)