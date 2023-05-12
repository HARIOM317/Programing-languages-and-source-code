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
      title: 'Flutter Rows and Columns',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
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
    return Scaffold(
      appBar: AppBar(
        title: Text("Flutter Row and Column Widget"),
      ),
      body: Center(
        child: Container(
          width: 350,
          height: 500,
          child: Column(
            // mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text("S.No", style: TextStyle(color: Colors.lightBlueAccent, fontSize: 18),),
                  Text("Name", style: TextStyle(color: Colors.lightBlueAccent, fontSize: 18),),
                  Text("Gender", style: TextStyle(color: Colors.lightBlueAccent, fontSize: 18),),
                  Text("Age", style: TextStyle(color: Colors.lightBlueAccent, fontSize: 18),),
                  Text("Contact", style: TextStyle(color: Colors.lightBlueAccent, fontSize: 18),),
                ],
              ),

              Text('1.'),
              Text('2.'),
              Text('3.'),
              Text('4.'),
              Text('5.'),
              ElevatedButton(
                onPressed: (){
                  print("Button Clicked!");
                },
                  child: Text("Click Me!"),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
