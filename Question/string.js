function reverserString(string){
    let reverse = ""
    let length = string.length-1

    while (length>=0) {
        reverse = reverse+string[length]
        length = length-1
    }
    return reverse
}
console.log(reverserString("Hello"))

function isVowel(string){
    let count = 0;
    const vowels = "aeiouAEIOU"

    for (let index = 0; index <string.length; index++) {
        if (vowels.includes(string[index])) {
            count +=1;
        }
        
    }
    return count;
}

console.log(isVowel('hello'))





const vowels = "aeiou"
console.log(vowels.toLowerCase())
console.log(vowels.includes("a"))
console.log(['apple',"banana"].includes("banana"))



class 
