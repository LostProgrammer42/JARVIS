import os
def check(r):
    with open("Inventory.txt", "r") as input:
        for line in input:
            l=line.split(",") 
            if len(l)>1:
             if l[0] ==r:
                 print("The item exists")
                 print(f'Quantity: {l[1]}')
                 print(f'Box number: {l[2]}')
  
if __name__ == "__main__":
    while True:   
     k=input("Enter Item Name: ")
     check(k)