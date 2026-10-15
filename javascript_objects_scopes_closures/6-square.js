#!/usr/bin/node
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const character = c === undefined ? 'X' : c;
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log(character.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
