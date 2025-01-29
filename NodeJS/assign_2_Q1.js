
var fs=require('fs');

// Checking wheather file exists . If not then it will create new one. 
// If it exists then append the data to existing one.
var checkFile=fs.existsSync('./log.txt');
if(checkFile){
    fs.appendFile('log.txt','New appended text \n',function(err){
        console.log("Appended the existing file !");
    });
}
else{
    fs.writeFile('log.txt','This is a log file\n',function(err){
        console.log("Created new file !");
    });
}

