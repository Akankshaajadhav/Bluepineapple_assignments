//Array Manipulation


//Creating array of 10 integers
let arr=[14,33,6,96,35,28,64,59,47,71];

function results(arr) {
    //To find the largest number in the array
    console.log(`The largest number in the given array is : ${Math.max(...arr)}`);
    
    //To find the smallest number in the array
    console.log(`The smallest number in the given array is : ${Math.min(...arr)}`);

    //To calculate average of numbers in the array
    let sum=0;
    for(let i=0;i<10;i++){
        sum+=arr[i];
    }
    console.log(`The average of numbers in array is : ${sum/10}`);
}

//calling above function
results(arr);
