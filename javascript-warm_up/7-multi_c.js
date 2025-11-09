#!/usr/bin/node
const x = Number(process.argv[2]);

if (isNaN(x) || x < 1) {
  console.log('Missing number of occurrences');
} else {
  let out = '';
  for (let i = 0; i < x; i++) {
    if (i === 0) {
      out = 'C is fun';
    } else {
      out = out + '\n' + 'C is fun';
    }
  }
  console.log(out);
}
