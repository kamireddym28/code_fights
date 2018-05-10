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
