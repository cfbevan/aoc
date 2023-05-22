import {parseString, wrappingPaper, pt1, ribbon, pt2} from "../src/index"

test("parse", () => {
    expect(parseString("2x3x4")).toEqual({l:2, w:3, h:4});
});

test("wrappingPaper ex1", () => {
    expect(wrappingPaper({l:2, w:3, h:4})).toBe(58);
});

test("wrappingPaper ex2", () => {
    expect(wrappingPaper({l:1, w:1, h:10})).toBe(43);
});

test("p1 ex1", () => {
    expect(pt1("2x3x4")).toBe("58");
});

test("p1 ex2", () => {
    expect(pt1("1x1x10")).toBe("43");
});

test("p1 ex1 & ex2", () => {
    // Testing the sum function
    expect(pt1("2x3x4\n1x1x10")).toBe("101");
});

test("ribbon ex1", () => {
    expect(ribbon({l:2, w:3, h:4})).toBe(34);
});

test("ribbon ex2", () => {
    expect(ribbon({l:1, w:1, h:10})).toBe(14);
});

test("p2 ex1", () => {
    expect(pt2("2x3x4")).toBe("34");
});

test("p2 ex2", () => {
    expect(pt2("1x1x10")).toBe("14");
});

test("p1 ex1 & ex2", () => {
    // Testing the sum function
    expect(pt2("2x3x4\n1x1x10")).toBe("48");
});