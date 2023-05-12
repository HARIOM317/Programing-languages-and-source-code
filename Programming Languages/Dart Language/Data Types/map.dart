void main(List<String> args) {
  /*
    Dart Map is an object that stores data in the form of a key-value pair. Each value is associated with its key, and it is used to access its corresponding value. Both keys and values can be any type. In Dart Map, each key must be unique, but the same value can occur multiple times. The Map representation is quite similar to Python Dictionary.
   */

  var student = {'name': 'Hariom', 'age': 20, 'id': 201022, 'cgpa': 9.1};
  student['course'] = 'B.Tech';
  student['branch'] = 'CSE';
  print(student);
  print("The keys are : ${student.keys}");
  print("The values are : ${student.values}");
  print("The length are : ${student.length}");
  print("isEmpty : ${student.isEmpty}");
  print("isNotEmpty : ${student.isNotEmpty}");

  // Methods
  student.addAll({
    'mobile no.': 9302765839,
    'email': 'hariommewada484@gmail.com',
    'gender': 'mail'
  });

  student.remove('age');
  print(student);
  print("Name = ${student['name']}");
}
