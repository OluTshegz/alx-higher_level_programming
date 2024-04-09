#!/usr/bin/node
/**
 * Square class that inherits from previous square class
 */
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const myChar = c;
    if (myChar === undefined) { this.print(); } else {
      for (let i = 0; i < this.height; i++) {
        let myVar = '';
        let j = 0;
        while (j < this.width) {
          myVar += myChar;
          j += 1;
        }
        console.log(myVar);
      }
    }
  }
}
module.exports = Square;
