"use strict"; 

function outputAllItems(items) {
    console.log(items)
    for (const item of items) {
        console.log(item)
    }
}

// console.log(outputAllItems([1,2,3, 'test']))

function getAllEvens(nums) {
    const evenNums = [];
    for (const num of nums) {
        if (num % 2 === 0) {
            evenNums.push(num);
        }
    }
    return evenNums;
}

// console.log(getAllEvens([1,2,3,4,5,6,7]))

function getOddIndices(items) {
    let result = [];
    for (let i = 0; i < items.length; i++) {
        if (i % 2 !== 0) {
            result.push(items[i])
        }
    }
    return result
}
// console.log(getOddIndices([0,"one",2,"three",4,"five"]))


function printAsNumberedList(items) {
    let result = [];
    for (let i = 0; i < items.length; i++) {
        result.push((items.indexOf(items[i])+1).toString() + '. ' + items[i])
    }
    return result
}

// console.log(printAsNumberedList(['red', 'orange', 'yellow', 'green', 'blue']))

function getRange(start, stop) {
    let result = []; 
    for (let i = start; i <= stop; i++) {
        result.push(i);
    }
    return result
}
// console.log(getRange(3, 8))