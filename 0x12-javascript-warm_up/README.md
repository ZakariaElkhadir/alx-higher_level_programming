# 0x12. JavaScript - Warm up

## General

Welcome to the JavaScript Basics repository! This README will guide you through the fundamentals of JavaScript programming. Whether you're a beginner or looking to refresh your knowledge, you're in the right place.

## Why JavaScript programming is amazing

JavaScript is an amazing programming language for several reasons:
- It's versatile: You can use JavaScript for web development, server-side programming, mobile app development, and more.
- It's easy to learn: JavaScript has a simple syntax and plenty of resources for beginners.
- It's widely used: JavaScript powers the majority of websites on the internet and has a large community of developers.
- It's constantly evolving: JavaScript frameworks and libraries are constantly being developed, making it a vibrant and exciting language to work with.

## How to run a JavaScript script

To run a JavaScript script, you need a JavaScript engine. You can run JavaScript code in a web browser, using Node.js, or in any environment that supports JavaScript execution.

For example, to run a JavaScript file called `script.js` using Node.js, you would run the following command in your terminal:

```bash
node script.js
```

## How to create variables and constants

In JavaScript, you can create variables using the `var`, `let`, or `const` keywords. Here's how you can create variables and constants:

```javascript
// Variables
var x = 10;
let y = 20;
const PI = 3.14;
```

Variables declared with `var` can be re-declared and re-assigned, variables declared with `let` can be re-assigned but not re-declared, and constants declared with `const` cannot be re-assigned or re-declared.

## What are differences between var, const and let

- `var`: Variables declared with `var` are function-scoped, meaning they are accessible anywhere within the function they are declared in.
- `let`: Variables declared with `let` are block-scoped, meaning they are accessible only within the block they are declared in.
- `const`: Constants declared with `const` are also block-scoped, and their value cannot be changed once assigned.

## What are all the data types available in JavaScript

JavaScript has several built-in data types, including:
- Number
- String
- Boolean
- Object
- Array
- Function
- Symbol
- Null
- Undefined

## How to use the if, if ... else statements

In JavaScript, you can use the `if` statement to execute a block of code if a condition is true, and the `if...else` statement to execute a different block of code if the condition is false.

```javascript
if (condition) {
  // code to be executed if the condition is true
} else {
  // code to be executed if the condition is false
}
```

## How to use comments

You can use comments in JavaScript to add notes or explanations to your code. Single-line comments start with `//`, and multi-line comments are enclosed between `/*` and `*/`.

```javascript
// This is a single-line comment

/*
This is a
multi-line comment
*/
```

## How to affect values to variables

You can assign values to variables using the assignment operator `=`.

```javascript
let x = 10;
```

## How to use while and for loops

In JavaScript, you can use `while` and `for` loops to iterate over a block of code multiple times.

```javascript
// While loop
while (condition) {
  // code to be executed
}

// For loop
for (initialization; condition; increment/decrement) {
  // code to be executed
}
```

## How to use break and continue statements

You can use the `break` statement to exit a loop prematurely, and the `continue` statement to skip the current iteration of a loop and continue with the next one.

```javascript
// Break statement
for (let i = 0; i < 5; i++) {
  if (i === 3) {
    break;
  }
  console.log(i); // Output: 0 1 2
}

// Continue statement
for (let i = 0; i < 5; i++) {
  if (i === 3) {
    continue;
  }
  console.log(i); // Output: 0 1 2 4
}
```

## What is a function and how do you use functions

A function is a block of code that can be called and executed at any point in your program. You can define a function using the `function` keyword, followed by the function name and parameters (if any).

```javascript
function greet(name) {
  console.log(`Hello, ${name}!`);
}

// Calling the function
greet('John'); // Output: Hello, John!
```

## What does a function that does not use any return statement return

If a function does not use a `return` statement, it implicitly returns `undefined`.

```javascript
function doSomething() {
  // code here
}

console.log(doSomething()); // Output: undefined
```

## Scope of variables

The scope of a variable determines where in your code that variable is accessible. In JavaScript, variables have either function scope or block scope, depending on how they are declared.

```javascript
function myFunction() {
  var x = 10; // Function-scoped variable
  let y = 20; // Block-scoped variable
}
```

## What are the arithmetic operators and how to use them

JavaScript has several arithmetic operators for performing mathematical calculations:
- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/`
- Modulus `%`
- Increment `++`
- Decrement `--`

```javascript
let x = 10;
let y = 5;

console.log(x + y); // Output: 15
console.log(x - y); // Output: 5
console.log(x * y); // Output: 50
console.log(x / y); // Output: 2
console.log(x % y); // Output: 0
```

## How to manipulate dictionary

In JavaScript, dictionaries are called objects. You can manipulate objects by adding, updating, or deleting key-value pairs.

```javascript
let person = {
  name: 'John',
  age: 30
};

// Adding a new property
person.city = 'New York';

// Updating an existing property
person.age = 35;

// Deleting a property
delete person.age;
```

## How to import a file

In JavaScript, you can import functions, variables, or classes from other files using the `import` statement (in modules) or by including the file directly (in non-module scripts).

```javascript
// Using import statement (in modules)
import { myFunction } from './myModule.js';

// Including file directly (in non-module scripts)
<script src="myfile.js"></script>
```

This concludes the JavaScript Basics README. Happy coding! 🚀
