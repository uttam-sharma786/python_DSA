

let arr = [3, 1, 2, 10, 1];
let sum = 0;  // Initialize sum
let newArr =[]

// for (let i = 0; i < arr.length - 1; i++) {
//     let res = arr[i] + arr[i + 1];
//     sum = sum+res;  // Add to sum correctly
//     console.log(res);
    

    

// }

// console.log("Total Sum:", sum); // Print final sum if needed


for(let i=1;i<arr.length;i++){
    arr[i]= arr[i]+arr[i-1]
}

    console.log(arr);
    