import {expect, test} from "vitest"
import * as challenge from "./challenge.js"

test("challenge", () => {
    for (let i = 0; i < 100; i++) {
        const out = challenge.run(i);
        if (i === 13) {
            expect(out.mul(new challenge.Vector(5, 2))).toEqual(new challenge.Vector(15, 8));
        } else if (i === 17) {
            expect(out()).toEqual(999555);
        } else if (i % 10 === 0) {
            expect(out).toEqual(10);
        } else if (i % 16 === 0) {
            expect(out).toEqual(16);
        } else {
            expect(out).toEqual(42);
        }
    }
})

