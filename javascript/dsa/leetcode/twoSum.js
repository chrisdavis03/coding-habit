/*
Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

- **Only one valid answer exists.**
*/

//O(n**2)
const twoSumBruteForce = (nums, target) => {
    //lets bruteforce it, and optimize later. 
    //since we know that only 1 answer exists, we can walk through the array and stop at the first success. 

    for (i=0; i<nums.length; i++) {
        // process.stdout.write(i+"")
        for (j=0; j<nums.length; j++)
            // process.stout.write(nums[j] + "\n")
            if (nums[i]+nums[j] === target ) {
                process.stdout.write("success:\t" + nums[i] + " + " + nums[j] + " = " + target + "\n")
                return ([i,j]);
            }
    };
};

const twoSum = () => {
    //i think we can use binary search to throw away a lot of test cases. 

    //there is no guantee that the array will be sorted.
    // s = nums.sort((a, b) => a - b)
    
    //find where i < target. If the array includes values greater that the target. 
    // We don't need to test them individually. 
};


const nums = [2,7,11,15]
const target = 9
process.stdout.write(twoSumBruteForce(nums, target) + "\n")
