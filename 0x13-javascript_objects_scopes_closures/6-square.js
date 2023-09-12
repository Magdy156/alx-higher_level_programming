#!/usr/bin/node
const BaseSquare = require('./5-square');
class Square extends BaseSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let width = '';
        for (let j = 0; j < this.width; j++) {
          width += c;
        }
        console.log(width);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
