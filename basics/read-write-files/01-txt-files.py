import csv


#read files 
def read_plain_text(path:str):
    #read plain text
    with open(path, 'r') as file:
        for line in file.readlines():
            print (line)

def count_lines_in_plain_text(path:str) -> int:
    #count audio streams
    stream_count = 0
    with open(path, 'r') as file:
        for line in file.readlines():
            if 'ID' in line[0:2]: 
                stream_count += 1
        print (stream_count)
        return(stream_count)
    
#write files


if __name__ == '__main__':
    #for testing different functions
    count_lines_in_plain_text('./data/rlj_aits_TRL_ATCWS_1080_2398_240_2ch_V1-R2.mov.mediainfo.txt')
