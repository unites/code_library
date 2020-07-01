import json

py_dictionary = {}

# Write Dict to Json
with open('file.json', 'w') as f:
    json.dump(py_dictionary, f, indent=4, sort_keys=True)

# Load Json into dict
with open('file.json') as f:
        py_dict = json.load(f)