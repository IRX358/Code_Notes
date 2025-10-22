// JavaScript notes with code from here
//JS needs runtime environments to run locally without browser like "Node js" "Deno" "Bun"
// Here using Node Js ---> To run your .js file use 'node filename.js'
//ANCHOR - To run one particular snippet select it and then "ctrl+r r" , if not selected then entire file will run

//NOTE 1] ___ Variables_____________
let ir = 220;
var ii = "22rr";
const hero = "IRX358";
ii = 885;
ab = "rerere";
/* 
Avoid using var declarations as it has issues with javascript block and functional scope  
As javascript is called as forgiving language we can declare variables without any prefix keywords as well .... and even semicolon usage is not mandatory
*/

console.log(ir);
console.table([ir, ab, ii, hero, ii]); // To log more than one value on console in the form of a table we use this

//NOTE 2] ___ Datatypes and ECMA standards___________
("use strict");
// using this above line at the start of each scrpit makes the java script code as the newer version and is a good practice to use it
alert(3 + 3); // we are using nodejs and this is only browser

// original documentation is on ecma script ..... all the standards are defined in here || but MDN referrence is best for simpler and better understandings
// JS is dynamically typed language .... will recognise the datatype as we assign it to a variable x

//Primitive datatypes
// they are callby value
/*
7 types : String , Number , Boolean , null , undefined , Symbol , BigInt

*/

let name = "ir" //string datatype
let age = 18 // number datatype ... ranges from 0 to 2^53 , can use bigInt datatype for larger numbers
let allow = false // boolean datatype 
let ab = null //standalone value ... representation of emptiness for a value
let a // will be having the value of undefined .... can have a value later , not assigned later
const id=Symbol('123')
const id2 = Symbol('123') 
console.log(id === id2); // will be false  
// symbol is also a value / datatype .... will be used when we have to uniqueness of a component during react mostly ...

// Reference types [Non - primitive]
// Arrays , Objects , Functions

const heros = ['iron man','hulk','thor'];
let obj ={
    name :"tony stark",
    persona :"philanthrophist",
    avenger_as :'Iron man',
    rank : 1
}
const myfun = function(){
    console.log("this is a sample function");    
}

//another non primitive datatype is " object"
typeof "ir" // to know what type is your value
typeof(83) // this syntax is also correct
typeof null // this says an object
typeof undefined // this says undefined only , cuz its a type in JS

//NOTE - 3]___ Conversion of datatypes ___________
let score = "88"
let vlu_score = Number(score) // this will be chamged as value 88 but 88a => NaN ; true => 1 ; null => 0 ;
let logg = 2
let bool_log = Boolean(logg) // will be true "" => false ; "aa" => true ; 0 => false
let num = 33
let str_num = String(num) // will be stringified

//NOTE - 4]___ Operations___________
let value = 3
let negvlaue = -value // will get negative of tht value
console.log(2+2); //add
console.log(2-2); //subtract
console.log(2*2); //multiple
console.log(2**2); // power of
console.log(2/2); // divide
console.log(2%2); // modulo

let str1 = "iir"
let str2 =" ffan"
let mane = str1 +str2 // concatenation
console.log("1"+2+2);// o/p : 122
console.log(2+1+"2");// o/p : 32 

//NOTE - 5]___ Conversions____________
/*
> , < , >= , <= .... are for comparisons ... if comparing string / other primitive datatypes with a number , the stirng and all willl be converted into numbers and then compared 
== ..... is the equality operator for comparisons ... this will also be converting other datatypes
=== ..... is the strict equal to ..... will compare datatypes as well and not be converting datatypes
*/

//NOTE 6] ___ Stack and Heap memory____________

/*
Primitive types <=uses=> stack memory <=when defined=> while using we get the copy of the value
Non-Primitive types <=uses=> Heap memory <=when defined=> while using we get the reference of the value

let name1 = "ir"
let name2 = name1 // now name2 will get the value of name1 by coppying which will be stored in STACK again
name2="jbl" // it will only change name2 and not name1 as in the value wass asssigned by coppying and not by referrence

let obj ={
    email="ir.358@gmail.com,
    upiId="ir358@fam";
    }
    
    let obj2 = obj1 // now the obj2 will be assigned a value by reference of the value of obj1 stored in HEAP
    
    obj2.email ="ir.358.786@gmail.com"

console.log(obj1.email) // o/p : ir.358.786@gmail.com ..... as in the value changed is same as the value stored for obj1 which was stored in HEAP
*/

//NOTE - 7]___ Strings__________
let namee = 'ir'
let projects = 5

console.log(namee +" has this many projects : "+projects); // pooor way of writing code
// Using backticks for the same is a more professional way
console.log(`Hello my name is ${namee.toUpperCase} and i have ${projects} projects donee ...`);

// another syntax to decalre a string .... by invoking an object
let namme = new String('IR358')
// commonly used str funs
/**
 .length 
 .toUpperCase()
 .charAt(2)
 .indexOf('t')
 .substring(st,end)
 .slice(st,end) // supports -ve start values which will loop on to last letters
 .trim() // removes white spaces ... has trimstart() and trimend() as well
 url.replace('%20','_')
 url.includes('.com')
 .split(' ')
 ...... and many more .... u can check out from the prototype of the string object

 usse this to see all the str funs / attributes .... .__proto__
 */


///NOTE 8] ___  Numbers and Maths _________

// another syntax to declare a number 
const blnc = new Number(100) 
// even numbers has a set functions like strings
blnc.toString()
console.log(blnc.toString().length);
console.log(blnc.toFixed(2)); // sets the number of decimals to 2 

const num2=122.834433
console.log(num2.toPrecision(3)); // it will set the precision to this many numbers , show only tht many set of numbers by rounding off    // o/p: 123

const huns=1000000000
console.log(huns.toLocaleString()); // this will add commas as per the number system of tens , hunderds , thousands .... // u can make this commas as per indian system as welll by .toLocalString('en-In')

// the MATH library comes by default with javascript
/**
 Math.abs(-4) // will give u the absolute value of this i.e, 4
 Math.round(4.6) // will round off as per the deccimal values
 Math.ceil(4.2)
 Math.floor(4.9)
 Math.pow(2,3)
 Math.min(4,3,2,5)
 Math.max(2,5,6,4,2)
 
 Math.random() // will give u a random value from 0 to 1
 u can do (Math.random()*10)+1 to generate values from 1 to 100
 
 u can generate values between range of 2 nos. like this
 const min=12
 const max=18
 
 Math.random() * (max-min+1) + min // this will generate values from 12 to 18 .... but with decimals ... to get a single digit u can do this....
 Math.floor( Math.random() * (max-min+1) + min )
 
 */

///NOTE - 9] ___ Date and Time____________
let d = new Date(); // o/p: 2025-08-28T03:57:45.564Z
// u can many funs with dates as u have with strings
console.log(d.toDateString()); // O/p: Thu Aug 28 2025
console.log(d.toLocaleDateString)(); // O/p: 8/28/2025
 console.log(d.toString()); // O/p: Thu Aug 28 2025 04:00:27 GMT+0000 (Coordinated Universal Time)
 
 const mydate = new Date(2023,0,23) // months start from 0 in javascript
 const mydate1 = new Date(2023,0,23,5,3) 
 const mydate2 = new Date("2023-01-14") 
 const mydate3 = new Date("01-14-2023") 
 
 console.log(mydate.toDateString()); // O/p: Mon Jan 23 2023

 //timestamps in js
const timestmps = Date.now()
console.log(timestmps); // O/p: 1756353989392
console.log(Math.floor(Date.now()/10000000)); // O/p: 175635

console.log(mydate3.getTime());// u can get time from this , as date is an object and has these values
newDate.getMonth()
newDate.getSeconds()
newDate.getDay()

newDat.toLocaleString('default',{
    weekday:"long",
    timezone: "IST"
})



///NOTE - 10] ____ Arrays____________
// Arrays in JS are resizable 
// can have elements with different data types
// indexing starts from zero

 const arr=[2,2,2,1,3,4,5,true,"ir"]
 const arr2 = new Array(1,2,3,4,5,6)

 //  Array methods 

 arr2.push(6)  
 arr2.pop()
 arr2.unshift(0) // will add element in the start of the array
 arr2.shift() // will remove ele from start
 arr2.includes(0) // RETURNS A BOOLEAN 
 arr2.indexOf(3)
 arr2.join() // will make a string of the elements of the array
 arr2.slice(1,5) // will return the subset of array st from 2nd pos till 5th pos ... ending is exclusive // original array is not altered or anyhthing 
 arr2.splice(1,5) // same as slice but ending is inclusive and this will remove those elemets from this original array
 arr2.push(arr) ; arr2.concat(arr) // this will add the whole arr as one single ele in arr2 ... // push will alter the arr2 and concat will not alter
 const newarr = [...arr2,...arr] // The SPREAD operator ... this will bring elements of both the arrays together into an newarr
 const deeparr = [1,2,3,[4,5,6],7,[6,7[4,5]]] // this kind of emmbeded array inside an array can be made into a single array by using this function
 const NodeepArr = deeparr.flat(Infinity) // n refers to depth of the flatness .... n can be 1,2,3... Infinity also
console.log(arr2)
console.log(newarr)
console.log(deeparr)
console.log(NodeepArr)
console.log(Array.isArray("Irx358")) // will return flase
console.log(Array.from("Irx358")) // will make and return a array of this 
// Array.of(num1,num2,num3) // num1,2,3 can be any variables...

//NOTE 11] ____ Objects____________

// Objects can be created in two ways - using Constructor and using literal || Singleton is created when objects created using constructors
// Object Literals
const mySm=Symbol("key1") //Declaring a symbol
const Jser={
    name:"ir" ,
    age:10,
    "one":"two", // this cant be acessed using JSUser.one
    [mySm]:"mykey", // using an symbol as the key in an object
    loc:"blore",
    online:false,
    lastseen:["mon","tue","fri"]
} 
// Accesing elements from object
console.log(Jser.lastseen);
console.log(Jser["one"]);
console.log(Jser["online"]);
console.log(Jser[mySm]); // Like this u can access a symbol key from an object

Jser.age=20 //Edting an value
// u can lock an object so tht it cant be changed later by using freeze func
// Object.freeze(Jser) // no changes in the objects will be considered after this

Jser.grting=function(){
    console.log("Heloo user");
    
}
console.log(Jser.grting); // this will only return the reference of the function 
console.log(Jser.grting()); // this will exctue the function as well

// to make function in a object which  use the other values of same onject 

Jser.grting2=function(){
    console.log(`Hello Js user , ${this.name}`);  // this. will find for the specifies value in the same object (`` backticks for string interpolation)
}
console.log(Jser.grting2());

// Creation of object using Constructor => Singleton

const Nser=new Object() // This is a singleton object

// nested Objects

Nser.email="ir.gmail.com"
Nser.names={
    sonname:{
        firstname:"irfan",
        lastname:"ir"
    },
    momname:{
        firstname:"mom",
        lastname:"ir"
    },
    dadname:{
        firstname:"dad",
        lastname:"ir"
    }
}
console.log(Nser.names.sonname.lastname);

// Combining objcets
const ob1={1:'a',2:'b'}
const ob2={3:'c',4:'d'}
const ob3={...ob1,...ob2} // This is best and cool way brooo (Spread operator)
const ob4=Object.assign({},ob1,ob2) // the first {} is a optional paramter which says an empty object is the target and all other are the soucres 
console.log(ob3);

// WHen u get values from databse we get it in the form of ArrayOfObjects
const data=[
    ob={
        id:1
    },
    obb={
        id:2
    },
    obbb={
        id:3
    }
]
// accessing these kinda things is like
data[1].id  //data[1] is an object || data is an array 
//u ccan get keys / values of from an object and they will be given in the form on arrays 
console.log(Object.keys(ob3));
console.log(Object.values(ob4)); // returns an array so u can iterate through them easily
console.log(Object.entries(ob4)); // returns an nested array of both keys and values
console.log(ob3.hasOwnProperty('4')); // to check if tht key exists
// check on prototype property for more methods on objects

// Destructuring of an object
// often while using REACT we have to destructure an object and take it's value 
// JSON - Java Script Object Notation
const course={
    crname:'react course',
    price:'999',
    instr:'hitesh'
}

// an pro way to extract values from a object
// {} syntax in JS is for destructuring
const{instr}=course // This way u can extract this value from the object and next time just use the value name to access
console.log(instr); // u dont have to calling it like course.instr 
const{instr:i}=course // This way u can extract this value from the object and next time just use the value name to access
console.log(i); // This like calling the object values with an alias

// When using APIs we would get values in the form of json 

//example json :
// {
//     'name':'ir',
//     'age':'20',
//     'intrest':'dance'
// }


// No more a beginner bro ..... Let's move ahead to Intermidiate





