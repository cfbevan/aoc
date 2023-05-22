import { readFileSync } from "fs";

interface IBox {
    l: number;
    w: number;
    h: number;
}

/**
 * Parse a string of form LxWxH in to an IBox object.
 * 
 * @param s String of form LxWxH.
 * @returns Parsed IBox data.
 */
export const parseString = (s: string): IBox => {
    const data = s.split("x");
    return {
        l: parseInt(data[0], 10),
        w: parseInt(data[1], 10),
        h: parseInt(data[2], 10),
    };
};

/**
 * Calculate the wrapping paper needed.
 * 
 * Sum of area of each face plus area of the smallest side.
 * 
 * @param box A parsed box string.
 * @returns Calculated wrapping paper needed.
 */
export const wrappingPaper = (box: IBox): number => {
    const values: number[] = [
        box.l * box.w,
        box.w * box.h,
        box.h * box.l
    ];
    return 2*values[0] + 2*values[1] + 2*values[2] + Math.min(...values); 
};

/**
 * Calculate the ribbon needed.
 * 
 * Shortest distance around the sides plus the cubic feed of volume of the box.
 * 
 * @param box A parsed box string.
 * @returns Calculated ribbon needed.
 */
export const ribbon = (box: IBox): number => {
    const values: number[] = [box.l, box.w, box.h].sort((a,b) => a - b);
    return values[0] + values[0] + values[1] + values[1] + values.reduce((p, c) => p*c, 1);
};

export const pt1 = (s: string): string => {
    // Parse all lines as boxes
    const boxes: IBox[] = s.split("\n").map(x => parseString(x))
    // Calculate paper needed for each box
    const paper: number[] = boxes.map(box => wrappingPaper(box));
    // Return sum of papers
    return paper.reduce((prev, current) => prev + current, 0).toString();
};

export const pt2 = (s: string): string => {
   // Parse all lines as boxes
   const boxes: IBox[] = s.split("\n").map(x => parseString(x));
   // Calculate paper needed for each box
   const ribbons: number[] = boxes.map(box => ribbon(box));
   // Return sum of papers
   return ribbons.reduce((prev, current) => prev + current, 0).toString();
};

if (require.main === module) {
    // Load file
    const data = readFileSync("input.txt").toString().trim()

    console.log(pt1(data))
    console.log(pt2(data))
}
