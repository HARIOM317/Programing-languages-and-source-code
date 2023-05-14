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
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: '3D List'),
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
  var arrIndex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  var colorIndex = [Colors.blue, Colors.blueAccent, Colors.indigo, Colors.indigoAccent, Colors.lightBlue, Colors.teal, Colors.tealAccent, Colors.cyan, Colors.lightBlueAccent, Colors.cyanAccent];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: ListWheelScrollView(
          itemExtent: 250,
          children: arrIndex.map((value) => Container(
            width: double.infinity,
            margin: EdgeInsets.all(10),
            
            decoration: BoxDecoration(
              color: colorIndex[value],
              borderRadius: BorderRadius.circular(20)
            ),

            child: Center(
              child: Text('Item ${value+1}', style: TextStyle(fontSize: 40, color: Colors.white, fontWeight: FontWeight.bold),),
            ),
          )).toList(),
        ),
      )
    );
  }
}
