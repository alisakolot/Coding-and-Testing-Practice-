// "use strict"; 

// // let person = {
// //     name: 'Al', 
// //     age: 25
// // };


// // Dot Notation
// person.name = "George";


// // Bracket notation: 
// let selection = "name";

// person[selection] = "mary";



// let flower = {
//     height: 10, 
//     color: "yellow", 
//     grow() {
//         this.height += 5;
//     }
// };

// flower.grow();
// // console.log(flower.height)

// let height = 4; 
// let strength = 100; 

// let warrior = {
//     height,
//     strength
// };

// function modulePattern() { 
//     function add() {

//     }
//     function subtract() {

//     }
//     return {
//         add, 

//     }
// }

// assign lets you take a source and multiple object
// extend: taking obj and merging them together 
// Object.assign:: method, first param is a target object you 
    // want to apply 
    // add the obj that you want to override last 
    // can be used to copy obj

// let person = {
//     name: 'Ryan', 
//     height: "185", 
//     strength: 100
// }; 

// let warrior = {
//     height: "200", 
//     strength: 1000
// };

// // merging objects together
// let myWarrior = Object.assign({}, person, warrior);
// console.log(myWarrior);

// reassign properties
// let person1 = {
//     name: "Ryan",
//     age: 21
// };

// Use Object.assign to copy objects 
// empty obj allows you to make new copy
// let person2 = Object.assign({}, person1);
// person2.name = "ben";
// console.log(person1)
// console.log(person2)

const user = {
    name: "Dom", 
    age: 32, 
    occupation: "Web Dev"
};
// keys method: gives you array of each property
// console.log(Object.keys(user))

// for (const key of Object.keys(user)) {
//     console.log(`${key} => ${user[key]}`);
// }

// values method, gives us an array of values 
// console.log(Object.values(user));

// Entries method: combo of two, get two dimensional array
// console.log(Object.entries(user));

// for (const entry of Object.entries(user)) {
//     console.log(`${entry[0]} => ${entry[1]}`)
// }


// Array Destructuring: 
// for (const [key, value] of Object.entries(user)) {
//     console.log(`${key} => ${value}`)
// }


// let student1 = {
//     firstName: "Steven", 
//     lastName: "Hancock", 
//     student: true, 
//     quiz1: 90, 
//     q2: 70, 
//     q3: "85", 
//     quiz4: 100, 
//     quiz5: 0
// };

// for (let key in student1) {
//     console.log(key);
//     console.log(student1[key]);
// };

// console.log(Object.keys(student1));
// console.log(Object.values(student1));
// console.log(Object.entries(student1));

// filter method: allows you to filter values you dont want from an array, return array
//  =>/arrow function: limited function expression, does not have its own bindings, doesnt have args, cannot be used as constructors
// isNaN: returns true if val is not a number
// const getScores = function(obj) {
//     return Object.values(obj).filter(val => !isNaN(val) && 
//     typeof (val !== 'boolean'));
// };

// let scores = getScores(student1);
// console.log(scores);