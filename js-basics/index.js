//This is how we write a comment!

//Check console in inspect element to 
//see this in website
//Alternatively, open up command prompt
//and run node index.js
console.log('Hello world!');

//Declare a variable
let shouldBeUndefined;
console.log(shouldBeUndefined);

//Initialise and declare a variable
let myStr;
myStr = 'myStr';
console.log(myStr);

//To make sure that a variable does NOT change
//We use a constant variable
const interestRate = 0.3;
//interestRate = 0.4 <-- Impossible
console.log(interestRate);

//Primitive types
let stringVar = "Heretic" //String literal
let numVar = 30; //Number literal
let boolVar = true; //Boolean literal
let undefinedVar = undefined; //Undefined literal
let nullVar = null; //None literal
console.log(stringVar);
console.log(numVar);
console.log(boolVar);
console.log(undefinedVar);
console.log(nullVar)


//Dynamic typing is used!
let numToVar = "Two";
console.log(numToVar);
numToVar = 2;
console.log(numToVar);

//Let us put some variables into 
//an object
let person = {
    age: 21,
    adult: true
};

console.log(person);
//We can access certain fields too!
person.age = 22;
console.log(person.age);
person['age'] = 23;
console.log(person.age);


//Let us look at arrays now!
let selectedColours = ['nyekundu', 'buluu'];
console.log("selectedColours: " + selectedColours);
selectedColours.push('nyeusi');
console.log("After pushing, selectedColours: " + selectedColours);
console.log("At index 1 of selectedColours: " + selectedColours[1]);


//We can look at functions now
function greet(name) {
    alert(`Hello ${name}!`);
}

greet('Kenya')

function recursiveMultiply(val1, val2) {
    if (val1 > 0) {
        return recursiveMultiply(val1-1,val2)+val2;
    }
    else {
        return val1;
    }
    
}

alert(recursiveMultiply(17,4));