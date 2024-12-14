export class Vector {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    mul(other) {
        return new Vector(this.x * other, this.y * other);
    }

    add(other) {
        return new Vector(this.x + other.x, this.y + other.y);
    }

    sub(other) {
        return new Vector(this.x - other.x, this.y - other.y);
    }

    dot(other) {
        return this.x * other.x + this.y * other.y;
    }
}