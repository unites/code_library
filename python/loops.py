
planes = ["P40", "P51", "P38"]

# Iterate through Loop
n = 0
print("--Standard For Loop--")
for line in planes:
    print("List line number: " + str(n) + " Plane: " + line)
    n = n + 1

# Direct Call of List items
print("--Direct Call in List--")
print("List line 0: " + planes[0] + " | List item 1: " + planes[1] + " | List item 2:  " + planes[2])

# Python One line Loops
print("--One line loop iteration--")
[ print(p) for p in planes ]