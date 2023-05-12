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
        title: Text("Padding & Margin on Text Widget"),
      ),
      body: Container(
        margin: EdgeInsets.all(10),
        // padding: EdgeInsets.all(20),
        color: Colors.lightBlueAccent,

        child: Padding(
          padding: EdgeInsets.all(30),
          child: Text('Hello Flutter Developers', style: TextStyle(
            fontSize: 20,
            backgroundColor: Colors.tealAccent,
            fontWeight: FontWeight.bold,
          ),
          ),
        ),
      ),
    );
  }
}
