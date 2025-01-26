import { readFileSync } from "fs";

export const pt1 = (s: string): number => {
    return 0;
}

export const pt2 = (s: string): number => {
    return 0;
}


if (require.main === module) {
    // Load file
    const data = readFileSync("input.txt").toString()

    console.log(pt1(data))
    console.log(pt2(data))
}
