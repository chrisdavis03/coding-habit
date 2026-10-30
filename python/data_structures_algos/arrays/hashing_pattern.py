import string

# Use a hash map to store element frequecies
def frequency_counter(s: str):
    seen = {} # store counts by character
    #remove spaces, make lowercase, and strip punctuation
    n = s.replace(" ", "").lower().translate(str.maketrans("", "", string.punctuation))

    for i, ch in enumerate(n):
        seen[ch] = seen.get(ch, 0) + 1 
    
    print (seen)

# Group Anagrams - LC 49
'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
def group_anagrams(strs:list[str]):
    '''
    We need a hash map to store and lookup what we have seen.
    We should sort the str and use that as a key to lookup if we have seen an anagram of the current. 
    If the key exists, we store the current value in that key. 
    Then we build an array from the hashmap to return a grouped list. 
    '''
    seen = {}
    
    for i, s in enumerate(strs):
        k = "".join(sorted(s))
        seen[k] = seen.get(k, [])
        seen[k].append(s)
    
    result = []
    for i, a in enumerate(seen.values()):
        result.append(a)
    return result

if __name__ == '__main__':
    group_anagrams(strs = ["eat","tea","tan","ate","nat","bat"])

