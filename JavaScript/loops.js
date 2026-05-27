const num =[1,2,3,4,5];
for (let i = 0; i < num.length; i++) {
    console.log(num[i]);
}

let y = 5;
while (y > 0) {
    console.log(y);
    y=y-1;
}
// const numbers = [1, 2, 3, 4, 5];
for (let i = 0; i < num.length; i++) {
    if (num[i] % 2 === 0) {
        console.log(num[i] );
    }
}

// const avela =[1,2,3,4,5];
let ans=0;
for (let i = 0; i < num.length; i++) {
    ans += num[i];
}
console.log("Sum of elements in an array: " + ans);