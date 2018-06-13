/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    while(true) {
      var sum = (a^b);
      var carry = (a&b)<<1; 
      if(b==0){
          return a;
      }
        a = sum;
        b = carry;
    }
};
