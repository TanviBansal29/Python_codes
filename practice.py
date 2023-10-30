import json

json_string = '{"name": "Alice", "age": 30}'
loaded_data = json.loads(json_string)
print(loaded_data)