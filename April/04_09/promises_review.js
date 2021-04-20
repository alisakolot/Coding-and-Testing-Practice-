// 
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Turning callbacks into promises~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

// Below is a simple callback function that takes two callbacks, one for success, one for error. 
// Checks two variables to make sure that either of them are true: if they are true, then there will be an error
    // if not, then there will be a success callback
    // For context: the function describes whether or not someone is distracted/doesn't want to watch a tutorial 

const userLeft = false
const userWatchingCatMeme = false 

function watchTutorialCallback(callback, errorCallback) {
    if (userLeft) {
        errorCallback({
            name: "User Left",
            message: ":("
        })
    } else  if (userWatchingCatMeme) {
        errorCallback({
            name: "User watching cat meme", 
            message: "WebDevSimplified < Cat"
        })
    } else {
        callback("Thumbs up and Subscribe!")
    }
}

watchTutorialCallback((message) => {
    console.log("Success:" + message)
}, (error) => {
    console.log(error.name + " " + error.messaage)
})