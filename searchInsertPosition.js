/*
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it 
were inserted in order. You may assume no duplicates in the array.

Eg1: Input: [1,3,5,6], 5
     Output: 2
     
Eg2: Input: [1,3,5,6], 2
     Output: 1
     
Eg3: Input: [1,3,5,6], 0
     Output: 0
*/

var searchInsert = function(nums, target) {
  var i;
  var n = nums.length;
  if (n === 0 || target<nums[0]) {
    return 0;
  }
  if (target>nums[n-1]){
    return n;
  }
  for (i=0;i<n;i++) {
    if (nums[i]===target){
      return i;
    }
    if (nums[i]<target&&nums[i+1]>target) {
      return i+1;
    }
  }
};
