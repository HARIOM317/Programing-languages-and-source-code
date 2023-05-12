// void function (sequence of parameters should be same during function calling)
manager1(int quty, String unit, String item) {
  print("$quty $unit of $item are ready");
}

// void function (sequence of parameters can be anything during function calling)
manager2({int? quty, String? unit, String? item}) {
  print("$quty $unit of $item are ready");
}

void main() {
  manager1(5, "pcs", "T-Shirt");
  manager2(item: "Suger", quty: 10, unit: "KG");
}
