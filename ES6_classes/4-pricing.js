import Currency from "./3-currency";

export default class Pricing {
  constructor(amount = 0, currency) {
    this.amount = amount; // Use the setter for validation
    this.currency = currency; // Use the setter for validation
  }

  get currency() {
    return this._currency;
  }

  set currency(currency) {
    if (!(currency instanceof Currency)) {
      throw new TypeError("Currency must be a class of Currency");
    }
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(amount) {
    if (typeof amount !== "number") {
      throw new Error("Amount must be a number");
    }
    this._amount = amount;
  }

  displayFullPrice() {
    const code = this.currency._code;
    const name = this.currency._name;
    return `${this.amount} ${name} (${code})`;
  }

  convertPrice(conversionRate) {
    return this.amount * conversionRate;
  }
}
