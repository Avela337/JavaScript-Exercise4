// let personal  = "red"
// if (personal === "red"){
//     console.log("potato");
// }else if (personal === "blue"){
//     console.log("this is a couch");
// }else if (personal === "green"){
//     console.log("The favourite colour is green");
// }
// else {    console.log("The color is not red, blue, or green");
// }
const vegetables = ["Lettuce", "tomato", "avocado", "carrot"];
let found = false;
for (let i = 0; i < vegetables.length; i++) {
    console.log((i + 1)+"." +(vegetables[i]));
    if (vegetables[i] === "avocado" || vegetables[i] === "carrot") {
        console.log("found: " + vegetables[i]);
        found = true;
    }
}
if (!found) {
    console.log("No avocado or carrot found.");
}