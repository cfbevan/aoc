import {pt1, pt2} from "../src/index"

test("p1 ex1", () => {
    expect(pt1("(())")).toBe(0);
});

test("p1 ex2", () => {
    expect(pt1("()()")).toBe(0);
});

test("p1 ex3", () => {
    expect(pt1("(((")).toBe(3);
});

test("p1 ex4", () => {
    expect(pt1("(()(()(")).toBe(3);
});

test("p1 ex5", () => {
    expect(pt1("))(((((")).toBe(3);
});

test("p1 ex6", () => {
    expect(pt1("())")).toBe(-1);
});

test("p1 ex7", () => {
    expect(pt1("))(")).toBe(-1);
});

test("p1 ex8", () => {
    expect(pt1(")))")).toBe(-3);
});

test("p1 ex9", () => {
    expect(pt1(")())())")).toBe(-3);
});

test("p2 ex1", () => {
    expect(pt2(")")).toBe(1);
});

test("p2 ex2", () => {
    expect(pt2("()())")).toBe(5);
});
