// console.log("Hello");

function divideTwoNumbers(num, den) {
  return num / den;
}

console.log(divideTwoNumbers(10, 0));

// ! Strng interpolation

function crazyString(something, someone, somewhere) {
  return `${someone} was looking for ${something} in general vicinity of ${somewhere}`;
}
console.log(crazyString("book", "sahil", "classroom"));

// ! Javascript Arrow functions

function areaCircle1(radius) {
  let pi = 3.14;
  return pi * radius * radius;
}

console.log(areaCircle1(4));

let areaCircle2 = (_) => {
  const pi = 3.14;
  return pi * radius * radius;
};

console.log(areaCircle2(5));

let areaCircle3 = (radius) => 3.14 * radius * radius;

console.log(areaCircle3(8));
