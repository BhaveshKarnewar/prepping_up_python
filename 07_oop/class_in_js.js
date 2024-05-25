class Auto {
  constructor(brand = "tata", model = "base") {
    (this.brand = brand), (this.model = model);
  }
}

class electric extends Auto {
  constructor(brand, model, batterySize) {
    super(brand, model);
    this.batterySize = batterySize;
  }
}

let myCar = new electric("asdfghjkl", "mbvcxz", "2kw");

console.log(myCar);
