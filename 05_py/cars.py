cars = ["Ford", "Audi", "Alfa Romeo", "Skoda", "Toyota"]

def contains_item(lst:list[str], item:str)->bool:
    for i in lst:
        if i == item:
            return True
    return False
    
def add_item(lst:list[str], item:str)->None:
    if not contains_item(lst,item):
        lst.append(item)

def find_item(lst:list[str], item:str)->list[int]:
    pole_indexu = []
    for i in range(len(lst)):
        if lst[i] == item:
            pole_indexu.append(i)
    return pole_indexu

def revert_items(lst:list[str])->list[str]:
    lst_rev=[]
    for i in range(len(lst)-1,-1,-1):
        lst_rev.append(lst[i])
    # lst = lst_rev NELZE
    for j in range(len(lst)):
        lst[j] = lst_rev[j]

# add_item(cars,"Skoda")
# cars.append("Skoda")
# print(cars, find_item(cars, "Skoda")) 
revert_items(cars)
print(cars)