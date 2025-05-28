import csv

#read files
def read_csv_files(path:str):
    with open(path, 'r') as file:
        for line in file.readlines():
            clean_line = ''.join(line.split())
            #still contains start charcter '\ufeff'
            print(clean_line.split(','))

def read_csv_with_module(path:str):
    #no need to process new lines 
    with open(path, 'r') as file: 
        csvFile = csv.reader(file)
        for line in csvFile:
            print (line)

#write files

if __name__ == '__main__':
    #for testing different functions
    read_csv_files('./data/xumo-MOV-Manifest.csv')
    # read_csv_with_module('./data/xumo-MOV-Manifest.csv')