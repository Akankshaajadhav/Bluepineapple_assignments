// Assignment 2 : Basic Arithmetic Operations and Conditional Statements

//Creation of variables
let number1=10;
let number2=7;

//Performing and displaying arithmetic operations 
console.log(`Results of operations performed - \n  Addition is : ${number1+number2}`);
console.log(`  Subtraction is : ${number1-number2}`);
console.log(`  Multiplication is : ${number1*number2}`);
let div=number1/number2;
console.log(`  Division is : ${div}`);

//Checking condition for division 
if(div<10)
    console.log("Division of given numbers is less than 10!");
else if(div>10)
    console.log("Division of given numbers is greater than 10!");
else
    console.log("Division of given numbers is exactly 10!");
