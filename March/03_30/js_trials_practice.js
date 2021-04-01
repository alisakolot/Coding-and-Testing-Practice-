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
// reminder:  let allows you to delare variables that are limited to the 
    // scope of the block statement/expression in which it's used
// 'in' lets you loop over indices
// 'of' lets you loop over elements

function censorVowels(word) {
    let vowels = ['a', 'e', 'i', 'o', 'u'];
    let result = '';
    // for (let i = 0; i < vowels.length; i++) {
    //     if (word.indexOf(vowels[i]) > -1) {
    //         console.log('false');
    //         result += word[i]        }
    // }
    for (let i=0; i < word.length; i++) {
        if (vowels.includes(word[i])) {
            console.log(word[i])
        } else {
            result += word[i]
        }
    }
    console.log(result)
}
// console.log(censorVowels('javascript'))

function snakeToCamel(string) {
    let camel = []; 
    let wordList = string.split("_");
    camel.push(wordList[0])
    
    for (let word of wordList.slice(1)) {
        camel.push((word[0].toUpperCase() + word.slice(1)));
    }
    return camel.join('');
}
// console.log(snakeToCamel('the_great_british_baking_show'))


// **********************************************
// function longestWordLength(words) {
//     const wordLengths = {};
//     let keys = [];
//     // for (const item of words) {
//     //     keys.push(item.length);
//     //     for (const num of keys) {
//     //         wordLengths.num  = item;
//     //     }
//     // }
//     for (let i=0; i < words.length; i++) {
//         for (let item in words) {
//             wordLengths[i] = {
//                 i : item
//             }
//         }
//     }
//     console.log(keys);
//     console.log(wordLengths)
// }

// console.log(longestWordLength(['thermos', 'book', 'headphones']))