// Q. Use setTimeout, setImmediate, and process.nextTick to demonstrate how the event loop handles tasks. Add a console log to show their execution order.

//setTimeout
setTimeout(function(){
    console.log("5. This text is result of setTimeout. Executed after 3 seconds!");
},3000);
console.log("1. SetTimeout() function will execute and display its results after waiting for specified time.");
console.log("And it does not block the remaining execution ! That;s why this text is printed initially\n");

//setImmediate
setImmediate(function(){
    console.log("4. This is result of setImmediate");
});
console.log("2. SetImmediate() function will execute and display its results immediately.");
console.log("Even though code is executing asynchronously, result of function is displayed immediately!\n");

//process.nextTick
process.nextTick(function(){
    console.log("3. This is result of process.nextTick!")
});