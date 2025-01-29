//ASSIGNMENT 1

var http=require('http');              // Using existing module
var module1=require('./helper');       // Creating module for accessing function from another file

result=module1.getMessage();
console.log(result);                   // Printing results from created module

const server=http.createServer((req,res)=>{
    console.log('req');
    res.write('Welcome to Node.js !');
    res.end();
})

server.listen(3000,()=>{
    console.log('Server running at localhost:3000')
})