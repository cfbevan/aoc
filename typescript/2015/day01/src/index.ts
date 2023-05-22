import { readFileSync } from "fs";

export const pt1 = (s: string): number => {
    let floor = 0;
    [...s].forEach(c => {
        switch(c) {
            case '(':
                floor += 1;
                break;
            case ')':
                floor -= 1;
                break;
        }
    });
    return floor;
}

export const pt2 = (s: string): number => {
    let floor = 0;
    let output = -1;
    [...s].forEach((c, i) => {
        switch(c) {
            case '(':
                floor += 1;
                break;
            case ')':
                floor -= 1;
                break;
        }
        if (floor < 0 && output === -1) {
            output = i + 1;
        }
    });
    return output;
}


if (require.main === module) {
    // Load file
    const data = readFileSync("input.txt").toString()

    console.log(pt1(data))
    console.log(pt2(data))
}
