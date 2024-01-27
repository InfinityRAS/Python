let string = "[[][][{}{}{((())))}}}{()))}]]" // any arbitrary string

let countObj = {
    '[':0,
    '{':0,
    '(':0,
    ')':0,
    '}':0,
    ']':0,
}

for (i in string) {
    countObj[string[i]]++
}

let newStr = "";

for (const key in countObj) {
    count = countObj[key]
    newStr += key.repeat(countObj[key])
}

console.log(newStr)

