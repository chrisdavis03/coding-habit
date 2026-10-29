
import string

def two_pointers(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return (left, right)
        if current < target:
            left += 1   # need a larger sum → move the smaller side
        else:
            right -= 1  # need a smaller sum → move the larger side
    return None

'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
'''

def valid_palindrome(s):
    if len(s) == 0:
        return False
    # Store cleaned string.
    n = s.replace(" ", "").lower().translate(str.maketrans("", "", string.punctuation))
    # Store result
    result = True

    left, right = 0, len(n) -1

    while left < right: 
        if n[left] == n[right]:
            left += 1
            right -= 1
        else: return False

    return result

if __name__ == '__main__': 
    print (valid_palindrome(f'This is a sentence, that has: punctuation!'))
    print (valid_palindrome(f'A man, a plan, a canal: Panama'))