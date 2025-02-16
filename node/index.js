var math = require("./math.js");

var operation = process.argv[2];
var value1 =  parseInt(process.argv[3]);
var value2 = parseInt(process.argv[4]);

if (operation== "add"){ 
    var result=  math.add(value1,value2);

    console.log(result);
}

