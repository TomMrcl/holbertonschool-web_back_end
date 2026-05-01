export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const species = this.constructor[Symbol.species];
    return new species();
  }

  static get [Symbol.species]() {
    return this;
  }
}
