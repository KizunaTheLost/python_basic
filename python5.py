i = 1
while i < 5:
    print("i = ", i)
    i+=1

i = 1
while i < 5:
    print("i = ", i)
    if i == 3:
        break
    i+=1


    # i = 1
# while i < 5:
    # print("i = ", i)
    # if i == 3:
        # break
    # i+=1




fruits = ["Apple", "Banana", "Coconut"]
for fruit in fruits:
    print("Fruit: ", fruit)

for fruit in fruits:
    print("Fruit: ", fruit)
    if fruit == "Banana":
        break
    print("Fruit: ", fruit)

for fruit in fruits:
    if fruit == "Banana":
        continue
    print("Fruit: ", fruit)

for x in range(len(fruits) + 1):
        print("Number = " , x)
for x in range(5):
        print("Number = " , x)
else:
     print("Game Over")

adjs = ["Red","Yellow","Brown"]
fruits = ["Apple","Banana","Coconut"]
for adj in adjs:
     for fruit in fruits:
          print(adj, fruit)




def my_function():
     print("Hello World 1")
     print("Hello World 2")

my_function()
my_function()

# parameter
def my_name(fname):
     print("My name is ", fname)

my_name("Anya")

def my_name2(fname, Lname)
     print("My name is ", fname, Lname)

my_name2("Anya", "Roger")
my_name2(Lname = "Roger", fname = "Anya")

def my_name3(Lname = "Roger"):
     print("My last name is ", Lname)

my_name3()
my_name3("Paul")

def my_fruits(fruits):
     for fruit in fruits:
          print(fruit)

fruits = ["Apple", "Banana", "Coconut"]
my_fruits(fruits)



def red_potion(hp):
     return hp + 50

print("HP: ", red_potion(100))
print("HP: ", red_potion(70))
