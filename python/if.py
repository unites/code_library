import os

# Check if Directory is there
if os.path.isdir(self.filter):
    print("Success")
else:
    print("fail")

# Check if file is there
if os.path.isfile(self.filter):
    print("Success")
else:
    print("fail")


