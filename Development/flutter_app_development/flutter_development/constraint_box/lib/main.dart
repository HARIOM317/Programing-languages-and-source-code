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

        title: Text("Constraint Box"),
      ),
      body: Center(
        child: ConstrainedBox(
          constraints: BoxConstraints(
            maxHeight: 200,
            maxWidth: 350,
            minWidth: 200,
            minHeight: 150
          ),
          child: Text("Dart Exceptions are the run-time error. It is raised when the program gets execution. The program doesn't report the error at compile time when the program runs internally and if Dart compiler found something not appropriate. Then, it reports run-time error and the execution of program is terminated abnormally. This type of error is called Exceptions.", style: TextStyle(
            fontSize: 25,
            overflow: TextOverflow.fade
          ),
          ),
        ),
      )
    );
  }
}
