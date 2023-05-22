#!/bin/bash

year=${PWD##*/}
day=${1##+(0)}
project=$(printf "day%02d" $1)
session="$AOC_SESSION"

mkdir ${project}

cd ${project}

# get input
curl -s "https://adventofcode.com/${year}/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

# add readme
touch README.md

echo -n '{
  "name": "aoc",
  "main": "index.ts",
  "scripts": {
    "test": "jest",
    "lint": "npx eslint . --fix",
    "main": "ts-node src/index.ts"
  },
  "devDependencies": {
    "@babel/core": "^7.21.8",
    "@babel/preset-env": "^7.21.5",
    "@babel/preset-typescript": "^7.21.5",
    "@types/jest": "^29.5.1",
    "@typescript-eslint/eslint-plugin": "^5.59.7",
    "@typescript-eslint/parser": "^5.59.7",
    "babel-jest": "^29.5.0",
    "eslint": "^8.41.0",
    "jest": "^29.5.0",
    "ts-node": "^10.9.1",
    "typescript": "^5.0.4"
  }
}' > package.json

echo -n '/* eslint-env node */
module.exports = {
  extends: ["eslint:recommended", "plugin:@typescript-eslint/recommended"],
  parser: "@typescript-eslint/parser",
  plugins: ["@typescript-eslint"],
  root: true
  env: {
    jest: true,
    node: true,
  },
};
' > .eslintrc.cjs

echo -n '{
  "compilerOptions": {
    "target": "es2016",
    "module": "commonjs",
    "rootDir": "./src",
    "strict": true,
    "skipLibCheck": true
  }
}' > tsconfig.json

echo -n "module.exports = {
  presets: [
    ['@babel/preset-env', {targets: {node: 'current'}}],
    '@babel/preset-typescript',
  ],
};" > babel.config.cjs

npm install

mkdir "src"

echo -n 'import { readFileSync } from "fs";

export const pt1 = (s: string): string => {
    return s;
}

export const pt2 = (s: string): string => {
    return s;
}

if (require.main === module) {
    // Load file
    const data = readFileSync("input.txt").toString().trim()

    console.log(pt1(data))
    console.log(pt2(data))
}
' > src/index.ts

mkdir "__tests__"

echo -n 'import {pt1, pt2} from "../src/index"

test("p1 ex1", () => {
    expect(pt1("")).toBe("");
});' > __tests__/test_index.ts
