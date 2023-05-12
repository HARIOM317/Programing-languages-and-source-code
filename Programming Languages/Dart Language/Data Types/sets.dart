/*
The Dart Set is the unordered collection of the different values of the same type. It has much functionality, which is the same as an array, but it is unordered. Set doesn't allow storing the duplicate values. The set must contain unique values.
*/

void main(List<String> args) {
  var mySet = <String>{
    "hariom",
    "abhishek",
    "sumit",
    "mehak",
    "himanshu",
    "rupesh"
  };
  mySet.add("pooja");

  // It will not add because set contains only unique items of same data type
  mySet.add("mehak");
  print(mySet);

  print("1st member of set : ${mySet.elementAt(0)}");
  print("Is contain rupesh : ${mySet.contains("rupesh")}");

  mySet.remove("himanshu");
  print(mySet);

  var mySet2 = <String>{"Ajay", "Ravi", "Sonu"};
  var mySet3 = <String>{"Karan", "Ramesh", "Ravi", "Saket", "Atul"};

  // Set Operations
  print("mySet2 union mySet3 = ${mySet2.union(mySet3)}");
  print("mySet2 intersection mySet3 = ${mySet2.intersection(mySet3)}");
  print("mySet2 difference mySet3 = ${mySet2.difference(mySet3)}");
}
