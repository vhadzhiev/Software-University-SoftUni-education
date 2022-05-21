function greatestCommonDivisor(x, y) {
    x = Math.abs(x);
    y = Math.abs(y);
    while(y) {
      let t = y;
      y = x % y;
      x = t;
    }
    
    console.log(x);
  }

  greatestCommonDivisor(15, 5);
  greatestCommonDivisor(2154, 458);