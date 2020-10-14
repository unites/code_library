
# Simple Class

class Plane:
    def __init__(self, model, country, p_type):
        self.model = model
        self.country = country
        self.ptype = p_type

    def print_model(self,descrip):
        print(descrip + self.model)

    def __str__(self):
        return "Plane Class"

## Set Model
p1 = Plane("P51", "US", "Fighter")
print("--1--")
print(p1.model)
print(p1.country)
print(p1.ptype)
print("--2--")
## Change Plane Model
p1.model = "P38"
print(p1.model)
print(p1.country)
print(p1.ptype)


## Call Class Function
p1.print_model("The plane Model is: ")

# Simple Fucntions
def tank(var):
    print("Printing the var you provided " + var)
    return "Modify and return " + var

print("--4--")
tank("Panzer")
print("--5--")
print(tank("Panzer"))