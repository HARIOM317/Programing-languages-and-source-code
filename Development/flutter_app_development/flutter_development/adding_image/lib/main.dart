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
      title: 'Flutter Image',
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
        title: Text("Adding Image in App"),
      ),
      body: Column(
        children: [
          Center(
              child: Container(
                height: 300,
                width: 200,
                child: Image.asset('assets/images/hariom.jpg'),
              ),
          ),
          
          Center(
            child: Container(
              height: 200,
              width: 300,
              child: Image.asset('assets/images/car.jpg'),
            ),
          ),
        ],
      ),
    );
  }
}
