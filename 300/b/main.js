const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let H, W;
let A = [];
let B = [];
let match = false;

rl.on('line', (line) => {
  if (!H) {
    [H, W] = line.split(' ').map(Number);
  } else if (A.length < H) {
    A.push(line.trim());
  } else if (B.length < H) {
    B.push(line.trim());
  }
  if (A.length === H && B.length === H) {
    for (let s = 0; s < H && !match; s++) {
      for (let t = 0; t < W && !match; t++) {
        let ok = true;
        for (let i = 0; i < H && ok; i++) {
          for (let j = 0; j < W && ok; j++) {
            if (A[(i - s + H) % H][(j - t + W) % W] !== B[i][j]) {
              ok = false;
            }
          }
        }
        if (ok) {
          console.log('Yes');
          match = true;
        }
      }
    }
    if (!match) {
      console.log('No');
    }
  }
});
