// JavaScript Intermeddiate notes with code from here
//JS needs runtime environments to run locally without browser like "Node js" "Deno" "Bun"
// Here using Node Js ---> To run your .js file use 'node filename.js'
//ANCHOR To run one particular snippet select it and then "ctrl+r r" , if not selected then entire file will run

//NOTE 1] ___Functions____
// Packaging of a set of code for resuability is concept called functions 
function sayname(){
    console.log('Hello.');
    console.log('Ir ... welcome');
}

sayname // this is a reference
sayname() // this is a execution 

function add(n1,n2 = 8){ // the input variables we take when we create a function is called "PARAMETERS" // n2=8 is a deafult value for a parameter
    let res=n1+n2
    console.log("results is");
    return res
}

add(3,5) // this variable which we pass into a function is called "ARGUMENTS"
// if u donot pass any argument for a paramter declared it will be taken as "undefined"

function calItems(n1,n2,...n){ // the ... syntax used here is called 'REST' operator (it is also called spread depending on use case)
    return n  // as the n here takes the rest of the arguments in the form of list , this returns as list
}
console.log(calItems(22,22,222,22222,222222,2324,2232));

// Handling of objects using functions

function hndlObj(anyobj){ // similarly one can handle arrays on functions
    console.log(`username is ${anyobj.name} and age is ${anyobj.age}`); // if the value in the object is 'Age'/'agess' instead of 'age' this will be undefined ....
} // and this is main reason ppl love TYPESCRIPT cuz it handles such type-safety / type-checking

const user={
    name:'ir',
    age:'20'
} 
hndlObj(user)
hndlObj({
    name:'ju',
    age:'15'
})

//NOTE 2] ___Scope________
// the most ignored declaration
// var ---> if declared in a block scope it can be accessed and edited outside the block scope as well , if declared in global scope then also can be edited in the block scope and is overwritten

// The most useful declaration
// let ---> if declared in a block will have its value only till tht block scope , can also be simultaneously declared in global scope and will have tht global value outside the block 
let a=20
if(true){
    let a=40 // if not declared then outer varibale value only will be considered
    console.log(`inner one : ${a}`);
}
a+=2
console.log(`outer one : ${a}`);

// The most non volatile declaration
// const ---> same as let but it cannot be edited once declared

const b=20
if(true){
    const b=40
    console.log(`inner one : ${b}`);
}
console.log(`outer one : ${b}`);


//NOTE 3] ___Hoisting_____
//  A single function can be written in two ways 
// 1. As an function

addo(4)
function addo(n){
    return n+1
}
// This will not return an {{ERROR}} as when hoisting the java script stores functions separately and even if we invooke a function before declaring it like this it will be caled normally from the tree branch which is storing the functions

const addt = function(n){
    return n+2
}
addt(3)
// This function if invoked before declaring will return an {{ERROR}} , as this whole ass function will be stored in a varible addt which is stored in the other branh of tree while hoisting js and will be declared line by line .



//NOTE 4] ___THIS & Arrow funcion________

const user1={
    uname:'ir',
    price:999,
    welcome:function(){
        // console.log(`${this.uname} welcome to the website`); // 'this' keyword is used to refer current context 
        console.log(this);
    }
}

user1.welcome() //when we print only 'this' keyword , we get the whole object in this line of context
user1.uname='srk'
user1.welcome()//when we print only 'this' keyword , we get the whole object in this line of context
console.log(this); // here we get an empty object cuz in this line there is nthg in the context

function mymy(){
    console.log(this); // here it gives a lot of vallues in this context of a function.
}
mymy()

function mynmy(){
    let uname='ir'
    console.log(this.uname); // here it gives undefined cuz the context works only in a object and not here
}
mynmy()

// Arrow function
// syntaxes 
const my2my = () => {}
() => {} 
// In the arrow function u can write a single line function and skip the 'return' keyword by not using {} amd instead using () or nthg
(n1,n2) => n1 +n2 //Ar function without a name without using return
let add2=(n1,n2)=> (n1+n2) //Ar function with a name and using () & no return                 // -----------VERY MUCH USED IN REACT --------------
let add2o=(n1,n2)=> ({uname:'ir'}) //Same as above but we are returning a object                 // -----------VERY MUCH USED IN REACT --------------
let add3=(n1,n2,n3)=>{ return n1+n2+n3} //u have to mention return when using {}

//NOTE 5] ___IIFE - Immediately Invoked Function Expressions_____________

// sometimes we want a function like Database connection to be invoked immediately or even we want to have an funciton hvaing its own scope and not be polluted by the global scope ..... tht is when we use IIFE syntax
// IIFE used to avoid the problem from declaration / variable in the global scope
// (.........) ---> WKT , This is a block / a variable having some value(object kinda thing) 
// () ---> WKT , This is used to invoke the function i.e. call it 

// so IIFE s/x : (...function...)(); ----> Always remember to terminate the invocation once done incase of IIFE

// so to immediately invoke a function we need to use a syntax like this :
(function conn(){ // Named IIFE
    console.log(`DB connected`);
})(); // this is like containing/wraping a function defenation in a block and then immediately invoking it useing ()

( ()=>{
    console.log(`Arrow DB connected`);
})(); // same it is .. this also workss

a=( ()=> ('return statement this is'))(); // storing the return statement into a variable ... this also works
console.log(a);

( (uname)=>{  // fn excepting an parameter
    console.log(`Arrow DB connected by ${uname}`);
})('ir'); // Passing of the argument which is being excepted

//NOTE 6] ___Call Stack & JS Exection Context____

// [CODE] --> Global Exe Context --- will be refered to ---> 'this'
