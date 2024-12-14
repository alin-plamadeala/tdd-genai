import {describe, expect, test} from "vitest"
import * as vector from "./vector.js"


describe('Vector Test', () => {
    test("Constructor", () => {
        const vec = new vector.Vector(2, 4);

        expect(vec.x).toEqual(2);
        expect(vec.y).toEqual(4);
    })

    test("Mul", () => {
        const vec = new vector.Vector(2, 4);
        const other = 2;

        const result = vec.mul(other);

        expect(result.x).toEqual(4);
        expect(result.y).toEqual(8);
    })

    test("Addition", () => {
        const vec = new vector.Vector(2, 4);
        const other = new vector.Vector(3, 5);

        const result = vec.add(other);

        expect(result.x).toEqual(5);
        expect(result.y).toEqual(9);
    })

    test("Subtraction", () => {
        const vec = new vector.Vector(2, 4);
        const other = new vector.Vector(3, 5);

        const result = vec.sub(other);

        expect(result.x).toEqual(-1);
        expect(result.y).toEqual(-1);
    })

    test("Dot", () => {
        const vec = new vector.Vector(2, 4);
        const other = new vector.Vector(3, 5);

        const result = vec.dot(other);

        expect(result).toEqual(26);
    })
});
