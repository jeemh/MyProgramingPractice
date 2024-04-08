const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const A = input[0].trim().split(' ').map(Number);
const B = input[1].trim().split(' ').map(Number);

B.sort((a, b) => a - b).reverse();

let childrenNum = A[0];
let snackNum = A[1];
let start = 1;
let end = B[0];
let ans = 0;
let mid;
let theNum;

while(start <= end) {
    mid = Math.floor((start + end)/2);
    theNum = 0;
    for(let count = 0 ; count < snackNum ; count++){
        if(B[count] < mid){
            break;
        } else {
            theNum += Math.floor(B[count]/mid);
        }
    }
    if(theNum < childrenNum){
        end = mid - 1;
    } else {
        ans = mid;
        start = mid + 1;
    }
}
console.log(ans);