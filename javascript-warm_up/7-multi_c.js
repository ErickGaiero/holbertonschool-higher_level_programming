#!/usr/bin/node
const x = Number(process.argv[2]);

if (process.argv[2] === undefined || isNaN(x)) {
  console.log('Missing number of occurrences');
} else if (x > 0) {
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
