// to create a program to find the length of an object

let obj = { // you can create any sample object
    name: "Aryan",
    class: "XI S1",
    recognised: "Topper of X"
}

let objLength = 0 // refers to length of given object
for (const key in obj) {
    objLength++
}

console.log(objLength)
