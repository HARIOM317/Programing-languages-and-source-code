/* 
Dart List is similar to an array, which is the ordered collection of the objects.
*/

void main(List<String> args) {
  // Fixed Length List
  var list = List<int>.filled(5, 0);
  list[0] = 100;
  list[1] = 200;
  list[2] = 300;
  list[3] = 400;
  list[4] = 500;

  // updating list
  list[0] = 111;

  print(list);

  // Growable List
  var list1 = [10, 20, 30, 40.05, true, "hariom"];
  // add method
  list1.add(60);
  list1.add(70);
  list1.add(80);

  //  addAll method
  list1.addAll([11, 22, 33, 44, 55]);

  // insert method
  list1.insert(1, 100);
  list1.insert(0, 300);

  // insertAll method
  list1.insertAll(0, [55, 155, 255]);
  print(list1);

  list1.replaceRange(0, 5, [1, 2, 3, 4, 5]);
  print("\nAfter Replace Element");
  print(list1);

  // Removing Methods
  // remove()
  list1.remove(100);

  // removeAt()
  list1.removeAt(0);

  // removeLast()
  list1.removeLast();

  // removeRange()
  list1.removeRange(0, 5);
  print("\nAfter Removing Element");
  print(list1);
}
