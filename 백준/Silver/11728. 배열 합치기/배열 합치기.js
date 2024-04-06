const fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const A = input[1].trim().split(' ').map(Number);
const B = input[2].trim().split(' ').map(Number);

let pointerA = 0;
let pointerB = 0;
const C = [];

while (pointerA < A.length && pointerB < B.length) {
    if (A[pointerA] < B[pointerB]) {
        C.push(A[pointerA++]);
    } else {
        C.push(B[pointerB++]);
    }
}

while (pointerA < A.length) {
    C.push(A[pointerA++]);
}

while (pointerB < B.length) {
    C.push(B[pointerB++]);
}

console.log(C.join(' '));
