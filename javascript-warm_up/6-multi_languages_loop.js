#!/usr/bin/node
const arr = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let text = arr[0];

for (let i = 1; i < arr.length; i++) {
  text = text + '\n' + arr[i];
}

console.log(text);
