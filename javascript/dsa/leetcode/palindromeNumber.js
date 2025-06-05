/*
https://leetcode.com/problems/palindrome-number

Given an integer, return true if x is a palendrome and false otherwise. 

x could be between -2.147B and 2.147B


# Thoughts
# I feel like there is a pure path way to do this. but we could also convert to an array, reverse and traverse indexes. 
*/

const isPalendrome = (x) => {
  let f = String(x);
  f = f.split("").map(Number);
  let b = f.toReversed();

  //   process.stdout.write(f + "\n" + b + "\n");

  let p = new Boolean();
  for (i = 0; i < f.length / 2; i++) {
    if (f[i] === b[i]) {
      p = true;
    } else {
      p = false;
      break;
    }
  }

  return p;
};

const example1 = 121;
const example2 = -121;
const example3 = 10;

process.stdout.write(isPalendrome(example1) + "\n");
process.stdout.write(isPalendrome(example2) + "\n");
process.stdout.write(isPalendrome(example3) + "\n");
process.stdout.write(isPalendrome(123456654321) + "\n");
