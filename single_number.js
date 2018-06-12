var singleNumber = function(nums) {
    var s=[];
    for (var i=0; i<nums.length; i++) {
        s = s^nums[i];
    }
    return s;
};
