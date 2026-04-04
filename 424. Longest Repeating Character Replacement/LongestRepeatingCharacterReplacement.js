/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let i = j = 0;
    let map = {};
    let maxWindow = 0;
    map[s[0]] = 1;

    while(j < s.length){
        if(isValidWindow(map, k)){
            maxWindow = Math.max(maxWindow, j - i + 1);
            ++j;
            map[s[j]] = !map[s[j]] ? 1 : ++map[s[j]];
        }
        else{
            --map[s[i]];
            ++i;
        }
    }
    return maxWindow;
};

var isValidWindow = function(map, k){
    let totalCount = 0;
    let maxCount = 0;
    for(let i = 0; i < 26; i++){
        let char = String.fromCharCode(i + 65);
        if(map[char]){
            totalCount += map[char];
            maxCount = Math.max(maxCount, map[char]);
        }
    }
    return ((totalCount - maxCount) <= k);
};