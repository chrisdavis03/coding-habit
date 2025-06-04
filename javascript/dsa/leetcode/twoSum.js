/*
https://leetcode.com/problems/two-sum/

Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

- **Only one valid answer exists.**
*/

// time complexity = O(n**2), space complexity = O(1)
const twoSumBruteForce = (nums, target) => {
    //lets bruteforce it, and optimize later. 
    //since we know that only 1 answer exists, we can walk through the array and stop at the first success. 

    for (i=0; i<nums.length; i++) {
        for (j=i+1; j<nums.length; j++)  //never test the same index that the outer loop is testing. 
            if (nums[i]+nums[j] === target ) {
                process.stdout.write("success:\t" + nums[i] + " + " + nums[j] + " = " + target + "\n")
                return ([i,j]);
            }
    };
};
const nums = [3,2,4]
const target = 6
// process.stdout.write(twoSumBruteForce(nums, target) + "\n") //  this is O(n**2) time complexity.

/*
Notes on improvements: 

time complexity = O(n**2), space complexity = O(1)

While I don't fully understand it, there is common pattern that signals that we can make an improvement here. 

We can trade off  some space complexity to bring down the time complexity, making this a O(n)for both the time and space complexities. 

store new variable for the current value, then calculate x = target - current value. If x exists in the array, then that is our answer. 
We need to remember what values we have seen and where those values exists in the original arrap.  This suggests the use of a map.
the map will record what values that we have see at what inddex. 
*/

const twoSumOptimized = (nums,target) => {
    const seen = new Map();
    for (i=0; i<nums.length; i++) {
        x = target - nums[i]
        let isSeen = seen.get(x)
        if ( isSeen != i && isSeen != undefined){
            return [i, isSeen]
        } else {
            seen.set(nums[i], i)
        }
    };
}


const numsA = [3,3]
const targetA = 6

process.stdout.write(twoSumOptimized(numsA, targetA) + "\n")