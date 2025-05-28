import json

#read files
def read_json(path):
    'load file object directly to dict'
    with open(path, 'r') as file:
        data=json.load(file)

    print (data)
    return data

#write json
def write_json_file(out_path):
    data = {'users': [
        {'first_name': 'Chris', 'last_name': 'Davis', 'city': 'Jersey City'},
        {'first_name': 'Ryan', 'last_name': 'Smelly', 'city': 'Jersey City'},
        ]}

    #write mode will overwrite files. 
    with open(out_path, 'w') as out_file:
        json.dump(data, out_file, indent=4)

if __name__ == '__main__':
    #for testing different functions
    # read_json('./data/ffprobe.json')
    write_json_file('./data/users.json')