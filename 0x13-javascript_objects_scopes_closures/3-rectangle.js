#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (height > 0 && width > 0) {
      this.height = height;
      this.width = width;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }
}

module.exports = Rectangle;
