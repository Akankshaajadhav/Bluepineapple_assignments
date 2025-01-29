//Q : BLOCKING FUNCTION RESULT

var fs=require('fs');

// Blocking function
var readData=fs.readFileSync('./log.txt','utf-8');
console.log("BLOCKING FUNCTION RESULT : ");
console.log(readData);
console.log("Blocking function has read the file synchronously. SO this text is printed after completing whole execution of reading file\n");

// Non-blocking function
fs.readFile('log.txt','utf-8',function(err,data){
    console.log(data);
});
console.log("NON-BLOCKING FUNCTION RESULT :  \nNon-blocking function has read the file asynchronously. SO this text is printed before completing whole execution of reading file");