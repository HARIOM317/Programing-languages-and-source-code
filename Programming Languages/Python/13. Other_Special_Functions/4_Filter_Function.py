list_1 = [12, 45, 98, 76, 1, 2, 3, 1, 3, 5, 4, 6, 7, 8, 10, 98, 534, 76, 435]
def is_Greater_10(num):
    return num>10

gt_than_10 = list(filter(is_Greater_10, list_1))
print("Numbers greater tha 10: ", gt_than_10)

def is_Loewr_10(num):
    return num<10

lw_than_10 = list(filter(is_Loewr_10, list_1))
print("Numbers lower than 10: ", lw_than_10)