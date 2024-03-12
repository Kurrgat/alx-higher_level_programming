#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    // If c is undefined, use the character 'X'
    const char = c || 'X';

    // Print the square using the specified character
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
