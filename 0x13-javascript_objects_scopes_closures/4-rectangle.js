#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (height > 0 && width > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print (c = 'X') {
    let i = 0;
    while (i < this.height) {
      console.log(c.repeat(this.width));
      i++;
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
}

module.exports = Rectangle;
