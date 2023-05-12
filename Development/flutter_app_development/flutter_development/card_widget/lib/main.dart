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
        title: Text("Card Widget"),
      ),
      body: Center(
        child: Card(
          // shadow
          elevation: 10,
          shadowColor: Colors.blue,
          margin: EdgeInsets.all(15),


          child: Container(
            width: 200,
            height: 200,
            child: Center(
              child: Text("Hello World", style: TextStyle(
                fontSize: 25,
                fontWeight: FontWeight.bold,
              ),),
            ),
          ),
        ),
      ),
    );
  }
}
