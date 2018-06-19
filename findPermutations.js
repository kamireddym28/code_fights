/*
Given an array, find the permutations(with all distinct elements) of all the elements in an array.

Eg: Input: [a,b,c]
    Output: [abc, bca, cab]
*/

function getPermutations(strVar) {
    // Is there only one character,
    // then there is only one permutation... return it!
    if (strVar.length < 2) return strVar;

    // array to hold permutations
    var permutations = [];

    for (var i=0; i<strVar.length; i++) {
        var char = strVar[i];

        // No duplicates, skip char if it's used already
        if (strVar.indexOf(char) != i)
            continue;

        var remainingString = strVar.slice(0,i) + strVar.slice(i+1,strVar.length);

        for (var subPermutation of getPermutations(remainingString))
            permutations.push(char + subPermutation)

    }
    return permutations;
}

console.log(getPermutations('abc'));
