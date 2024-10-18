#Python makes it easy to work with JSON data using the json module.

import json

# Convert Python object to JSON string
data = {"name": "Alice", "age": 30}
json_data = json.dumps(data)
print(json_data)

# Convert JSON string to Python object
python_data = json.loads(json_data)
print(python_data)
