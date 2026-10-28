def sliding_window(nums):
    left = 0
    for right in range(len(nums)):
        # expand window — add nums[right]
        
        # while window condition is violated, shrink from left
        while condition_broken():
            # remove nums[left]
            left += 1
        
        # process current valid window
        # update result (max/min/length)

def longest_substring_without_repeats(s):
    left = 0
    result = 0

    if len(s) <= 1:
        return len(s)

    for right in range(left , len(s)+1):
        print (s[left:right])
        if (len(s[left:right]) != len(set(s[left:right]))):
            left +=1
        result = len(s[left:right])
            
    return result

if __name__ == "__main__":
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    s4 = "pp" # returns 1
    s5 = "mp" # returns 2
    s6 = "s" # returns 1
    s7 = "" # returns 0
    print (longest_substring_without_repeats(s5))



    
