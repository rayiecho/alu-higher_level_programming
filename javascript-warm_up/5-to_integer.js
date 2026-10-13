#!/usr/bin/node
const convertedInt = parseInt(process.argv[2], 10);

if (isNaN(convertedInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convertedInt);
}
