const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function sumOfArray(arr, end){
    var sum = 0;
    for(var i = 0; i<=end; i++)
        sum += arr[i];
    return sum; 
}

const A = input[0].trim().split(' ').map(Number);
const B = input[1].trim().split(' ').map(Number);

var startValue = Math.max.apply(null, B);
var endValue = sumOfArray(B, A[0]-1);
var midValue = Math.floor((startValue + endValue)/2);
var ans = midValue;

while(startValue<=endValue){
    var bucketCount = 0;
    var oneOfTime = 0;
    B.forEach(function(studyTime) {
        if(oneOfTime + studyTime > midValue){
            bucketCount += 1;
            oneOfTime = studyTime;
        } else {
            oneOfTime += studyTime;
        }
    });
    bucketCount += 1;

    if(bucketCount > A[1]){
        startValue = midValue +1;
        midValue = Math.floor((startValue + endValue)/2);
    } else {
        ans = midValue;
        endValue = midValue-1;
        midValue = Math.floor((startValue + endValue)/2);
    }
}

console.log(ans);