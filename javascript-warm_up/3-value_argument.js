#!/usr/bin/node
const value = process.argv[2];

if (value) {
  console.log(value);
} else {
  console.log('No argument');
}
