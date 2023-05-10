function eratosSieve(n) {
    if (n <= 1) {
        return []
    }
    const primes = new Array(n + 1).fill(true)
    primes[0] = false
    primes[1] = false
    for (let i = 2; i < Math.floor(Math.sqrt(n)) + 1; i++) {
        if (!primes[i])
            continue
        for (let j = i * 2; j < n + 1; j += i) {
            primes[j] = false
        }
    }
    const ret = []
    for (let i = 0; i < n + 1; i++) {
        if (primes[i]) {
            ret.push(i)
        }
    }
    return ret
}

function main() {
    const n = nextNum()
    const maxC = Math.floor(Math.sqrt(n)) + 1
    const primes = eratosSieve(maxC)
    let ans = 0

    for (let ai = 0; ai < primes.length - 2; ai++) {
        const aa = primes[ai] ** 2
        // 間にbを置かないといけないので、ai+2からスタート
        for (let ci = ai + 2; ci < primes.length; ci++) {
            const cc = primes[ci] ** 2
            const aacc = BigInt(aa) * BigInt(cc)
            // この時点でNを超えたら調べる必要がない
            if (aacc > BigInt(n)) break
            // ai+1からci-1まで探索
            for (let bi = ai + 1; bi < ci; bi++) {
                const b = primes[bi]
                const aabcc = BigInt(b) * aacc
                if (aabcc <= BigInt(n)) {
                    ans++
                } else {
                    break
                }
            }
        }
    }
    console.log(ans)
}

let inputs = "";
let inputArray;
let currentIndex = 0;

function next() {
    return inputArray[currentIndex++];
}
function nextNum() {
    return +next();
}
function nextBigInt() {
    return BigInt(next());
}
function nexts(length) {
    const arr = [];
    for (let i = 0; i < length; ++i) arr[i] = next();
    return arr;
}
function nextNums(length) {
    const arr = [];
    for (let i = 0; i < length; ++i) arr[i] = nextNum();
    return arr;
}
function nextBigInts(length) {
    const arr = [];
    for (let i = 0; i < length; ++i) arr[i] = nextBigInt();
    return arr;
}

// デバッグ環境がWindowsであれば条件分岐する
if (process.env.OS == "Windows_NT") {
    const readline = require("readline").createInterface({
        input: process.stdin,
        output: process.stdout,
    });
    readline.on("line", (line) => {
        inputs += line;
        inputs += "\n";
    });
    readline.on("close", () => {
        inputArray = inputs.split(/\s/);
        main();
    });
} else {
    inputs = require("fs").readFileSync("/dev/stdin", "utf8");
    inputArray = inputs.split(/\s/);
    main();
}
