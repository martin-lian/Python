'''
xname='{"name":"Martin","language":["English","Tamil"]}'
xname_dict=json.loads(xname)

print(xname_dict)
print(xname_dict["language"])

'''

import json
with open("data.json") as file:
    data = json.load(file)
    print(data)


"""
example = {
            "name":"lian",
            "s/o":"martin",
            "gender":"male"
          }
with open("filename.txt",'w') as json_file:
    json.dump("filename.txt",json_file)
    
"""

'''
# Assuming j_string contains your JSON string
j_string = '{"name": "John", "age": 30}'
parsed_data = json.loads(j_string)
print(parsed_data)
'''

'''
import json

# Specify the path to your JSON file
file_path = "data.json"

# Open the file in read mode
with open(file_path, "r") as file:
    data = json.load(file)

# Now 'data' contains the parsed JSON content
print(data)
'''