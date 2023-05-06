void main(List<String> args) {
  // Normal var (We can store only a single type of data)
  var name = "Hariom";
  // name = 98;   // it will throw an error
  name = "Sumit";
  print(name);

  // Dynamic var (We can store only different types of data)
  var data;
  data = "Hariom Singh Rajput";
  data = 89;
  data = true;
  data = 98.989;
  print(data);

  // Another way of dynamic data type
  dynamic data2 = "Hariom";
  data2 = 98;
  data2 = true;
  print(data2);
}
