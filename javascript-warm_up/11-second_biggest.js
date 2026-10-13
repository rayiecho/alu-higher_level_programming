#!/usr/bin/node
const args = process.argv.slice(2).map(Number).filter(num => !isNaN(num));

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  // Filter duplicates to find true second biggest if needed, or simply unique ranking
  const uniqueArgs = [...new Set(args)];
  if (uniqueArgs.length < 2) {
    console.log(0);
  } else {
    console.log(uniqueArgs[1]);
  }
}
