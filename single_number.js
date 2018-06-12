/*
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Eg1: Input: [2,2,1]
     Output: 1
Eg2: Input: [4,1,2,1,2]
     Output: 4
*/

var singleNumber = function(nums) {
    var s=[];
    for (var i=0; i<nums.length; i++) {
        s = s^nums[i];
    }
    return s;
};
