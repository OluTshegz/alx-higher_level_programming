#!/usr/bin/node
/**
 * Defines a rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      let j = 0;
      while (j < this.width) {
        rect += 'X';
        j += 1;
      }
      console.log(rect);
    }
  }

  rotate () {
    let temp = 0;
    temp = this.width;
    // [this.width, this.height] = [this.height, this.width];
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
    // [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}
module.exports = Rectangle;
