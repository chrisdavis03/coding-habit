import random

def generate_random_unsorted_list():
    arr = []
    arrSize =  random.randint(0, 500)
    #arrStart = random.randint(-500, 500)
    # arrEnd = random.randint(-500, 500)
    for i in range(0, arrSize, 1): 
        arr.append(random.randint(-500, 500))
        
    return arr

def generate_random_sorted_list(): 
    arr = generate_random_unsorted_list()
    arr.sort()
    return arr
    
if __name__ == '__main__': 
    #print (generate_random_unsorted_list())
    #print (generate_random_sorted_list())
    pass
