#!/usr/bin/node
function factorial (a) {
  let sum = 1;
  if (isNaN(a) || a === 1) {
    return (1);
  }
  for (let i = a; i > 0; i--) {
    sum *= i;
  }
  return (sum);
}
console.log(factorial(parseInt(process.argv[2])));
