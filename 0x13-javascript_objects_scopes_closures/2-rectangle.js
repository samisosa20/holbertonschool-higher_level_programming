#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (height > 0 && width > 0) {
      this.height = height;
      this.width = width;
    }
  }
}

module.exports = Rectangle;
