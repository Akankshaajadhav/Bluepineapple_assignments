
var fs=require('fs');
function fetchData() {
    let promise=new Promise((resolve,reject)=>{
        setTimeout(function(){
            var checkFile=fs.existsSync('./assignment10.js');
            if(checkFile){
                resolve("Exists");
            }
            else{
                reject("Doesn't exist");
            }
        },2000);

    })

    promise.then((message)=>{
        console.log("Your file "+ message);
    }).catch((message)=>{
        console.log("Your file "+ message);
    })
}

fetchData();
