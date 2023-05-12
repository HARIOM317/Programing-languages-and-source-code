import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter ListTile Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blueGrey,
      ),
      home: const MyHomePage(title: 'Flutter List Tile Widget Demo'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {

    var arrNames = ["Hariom", "Abhishek", "Aman", "Shubham", "Sumit", "Himanshu", "Rupesh", "Ravi", "Atul", "Mehak", "Aachal", "Pooja"];

    var numbers = ['9876235410', '7654389103', '8732109873', '9712345620', '4251230987', '7898221098', '9876523456', '9876987632', '8866889092', '7612321098', '9877654312', '9988776655'];

    return Scaffold(
      appBar: AppBar(
        title: Text("My Contact"),
      ),
      body: Container(
        color: Colors.white70,
        child: ListView.separated(itemBuilder: (context, index) {
          return ListTile(
            leading: Text('${index+1}'),
            title: Text(arrNames[index]),
            subtitle: Text(numbers[index]),
            trailing: Icon(Icons.add),
          );
        },

          itemCount: arrNames.length,
          separatorBuilder: (context, index){
          return Divider(height: 30, thickness: 3,);
          },
        ),
      )
    );
  }
}
