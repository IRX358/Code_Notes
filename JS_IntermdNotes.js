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
// Global execution context is different for different environments --> Bun,Dino,Browser,Nodejs
// 'this' value for a browser is 'Window Object'

// we have 3 exe contexts
// Global Exe Context , Function Exe Context , Eval Exe Context

// 2 phases in exe ---> 1.Memory Creation Phase 2.Execution Phase

// let's see step by step ki how a JS code is executed with an example 

let v1=10
let v2=20
function sum(n1,n2){
    let total = n1+n2
    return total
}
let res1=sum(v1,v2)
let res2=sum(25,25)

// When the above example is executed using a node env

// Step1: An Global execution (Global env) context is made --- and reference given to 'this'
// Step2:Memory Creation Phase => All the variables are just taken into consideration with default initialization (like this)
        // 1st cycle
                // v1<-undefined
                // v2<-undefined
                // sum<- fn defination
                // res1<-undefined
                // res2<-undefined
// Step3:Execution Phase => Vlaues will be assigned ,
        // 2nd cycle
                // v1<-10
                // v2<-5
                // sum<- [ new variable env
                //         Execution Thread ] (Another executional context will be createdd )
                // This above | executional context will have its own memory creation and execution phasses   
                //            | ------------>  Memory Phase      |   Execution context
                //                            n1 <- undefined    |   n1 <- 10      
                //                            n2 <- undefined    |   n2 <- 20      
                //                           total <- undefined  |   total <- 30     ( this will be returned back to its parent executional context and then it global executional)
                // Now after this operation this executional context will be deleted 
                // res1<-30 
                // res2<- ( again a new executional context will be created with 2 phases then the return value will be taken) 
       //            |-------   // sum<- [ new variable env
                                //         Execution Thread ] (Another executional context will be createdd )
                                // This above | executional context will have its own memory creation and execution phasses   
                                //            | ------------>  Memory Phase      |   Execution context
                                //                            n1 <- undefined    |   n1 <- 10      
                                //                            n2 <- undefined    |   n2 <- 20      
                                //                           total <- undefined  |   total <- 30     ( this will be returned back to its parent executional context and then it global executional)


// ====== Call Stack =====
//                      |                 |
// whenever a new fn    |                 |
//  is sent for exe.    |                 |
// ---> sum() [Push]--> |                 | ---> after exe. [POP] --->
//                      |_________________|
//                      |Global Execution |
//                      |     Context     |
//                      |_________________|
// 
//  As a stack follows LIFO approach , whenever a function in execution(already pushed in) calls another function inside it , the called function will will pushed in and then poped out and then after it's execution the main function will be executed and poped out
//  Similarly for n nested function calls ....



//NOTE 7] ___Control Flow____

// if-else statement 
let p=false
if (p){
    console.log("True");
} else {
    console.log("False");
}
// if shorthand
if (!p) console.log("False") 

// if-else-if statement 
let q=70
if (q>100){
    console.log("nah");
} else if(q<50) {
    console.log("nah");
} else{
    console.log("bingo");
}

// Switch case statement
let z=20
switch(z){
    case 5 :
        console.log("nah");
        break;
        case 10 :
            console.log("nah");
        break;
    case 15 :
        console.log("nah");
        break;
    case 20 :
        console.log("bingo");
        break; // JS is a old school language and after the match case the rest of the code will be executed if u dont write break here;
    case 25 :
        console.log("bingo");
        break;
        case 30 :
            console.log("bingo");
            break;
    default :
    console.log("not at all"); // only for default the break statement can be ignored
}

// Falsy values : 
//    1. false
//    2. 0
    //    3. -0
    //    4. BigInt (this datatype)
    //    5. Nan (Not a Number)
    //    6. "" (Empty string)
    //    7. null
    //    8. undefined
    //    9. 0n
    //   10. string.length === 0 (to check for empty string)
    //   11. Object.keys(our_obj).length === 0 (to check for empty object)

    // Truthy values : 
    //    1. true
    //    2. "0"
    //    3. 'false'
    //    4. " "
    //    5. []
    //    6. {}
    //    7. function(){}
    //    8. false == 0
    //    9. false == ''
    //   10. 0 == ''
    
// Nullish Coalescing Operator ( ?? ) : to safegaurd code from null / undefined

// under certain cases we might get 2 values for a single variable from the database , if such cases this operator is to make sure the varible takes the null or undefined values or if any complex functions recevied
let vl1;
// this assigns as per the null safety of the variable 
vl1 = 5 ?? 10 // 5 will be assigned
vl1 = null ?? 5 // 10 will be assigned
vl1 = undefined ?? 15 // 15 will be assigned
vl1 = null ?? 10 ?? 20 // 10 will be assigned 
// Basicallly this acts as the fallback for value assignment by assigning a flag value where a variable would probably get an null or undefined value

// Terniary Operator

// condition ? True : False
const ice =10
ice>20 ? console.log("expensive") : console.log("cheap")

//NOTE 8] ___Loops____