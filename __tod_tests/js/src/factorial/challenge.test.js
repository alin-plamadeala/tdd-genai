import {describe, expect, test} from "vitest"
import * as challenge from "./challenge.js"

describe("state", () => {
    test("a", () => {
        expect(challenge.run(0)).toBe(1)
    })

    test("b", () => {
        expect(challenge.run(1)).toBe(1)
    })

    test("c", () => {
        expect(challenge.run(2)).toBe(2)
    })

    test("d", () => {
        expect(challenge.run(3)).toBe(6)
    })

})