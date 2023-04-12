#leetcode 278 - first bad version

'''
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

constaints
1 <= bad <= n <= 2^31 - 1
'''

'''
Thoughts
The bad version will be somewhere betweeen 1 and 2.1 billion.

Version numbers start with 1

Since we need to find the first bad version. we will see a lot of bad versions. So we need to test n & n-1 for equality to ensure that its the first bad version. 
'''

def firstBadVersion(n:int) -> int:
    l, r = 0, n
    
    while l <= r:
        m = int(r-l)/2 + l