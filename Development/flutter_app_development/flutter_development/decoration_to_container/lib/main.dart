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
        title: Text("Decorating Container Widget"),
      ),
      body: Container(
        color: Colors.blue.shade50,
        width: double.infinity,
        height: double.infinity,
        child: Center(
          child: Container(
            width: 300,
            height: 300,
            decoration: BoxDecoration(
              color: Colors.blueGrey,
              // borderRadius: BorderRadius.circular(15),
              // borderRadius: BorderRadius.only(topLeft: Radius.circular(30), bottomRight: Radius.circular(30)),

              border: Border.all(
                width: 3, color: Colors.black,
              ),

              boxShadow: [
                BoxShadow(
                  blurRadius: 30,
                  // spreadRadius: 8,
                  color: Colors.black54
                ),
              ],
              shape: BoxShape.circle
            ),
          ),
        ),
      ),
    );
  }
}
