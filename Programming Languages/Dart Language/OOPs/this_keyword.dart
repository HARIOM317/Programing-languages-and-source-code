class Car {
  String name = "";
  double price = 0;

  Car(String name, double price) {
    this.name = name;
    this.price = price;
  }

  showDetail() {
    print("Name : $name");
    print("Price : Rs. $price");
  }
}

void main(List<String> args) {
  Car car = new Car("Range Rover", 6000000);
  car.showDetail();
}
