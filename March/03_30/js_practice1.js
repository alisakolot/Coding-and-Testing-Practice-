console.log('test run')

//1.  Object: Take object/write function into an array, where array only contains values
// let x ={
//     a:1, 
//     b:2,
//     };
// entries gives us a two dimensional array, not values
    // const xArr = Object.entries(x) 

// for (i in x) {
//     xArr.push(i);
// }
// console.log(xArr)

//2. 
// let x = "hi";

// // let y = "ih"; 

// // const reverseString = (str) => {
// //     str.split("").reverse().join("");
// // }
// // console.log(reverseString(x) === y)
// // take into account uppercase values 

// // 3. Object containing two methods, both do the same thing. find a way to console log
// // both a and b at the same time

// const Obj = {
//     a:1, 
//     b:2, 
//     getA() {
//         console.log(this.a);
//         },
//     getB() {
//         console.log(this.a);
//         }
//     };

// Obj.getA().getB();
    // Getting an undefined error
    // would not be able to run/get b, b/c b not a method of getA

    // What would you change so it would run? 
    //
// const Obj = {
//     a:1, 
//     b:2, 
//     getA() {
//         console.log(this.a);
//         return this;
//         },
        
//     getB() {
//         console.log(this.a);
//         }
//     };

//     Obj.getA().getB()

// 4. Given an array, wrte a function that creates a print function
[1,2].print();
Array.prototype.print = () => {
    console.log(`$this[0], ${this[1]}`);
}
Array.prototype.print = () => {
    let result = "";
    this.forEach(elem => {
        result += `${elem},`;
    })
    console.log(result);
}

