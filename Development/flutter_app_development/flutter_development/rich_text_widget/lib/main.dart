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
        title: Text("Rich Text Widget"),
      ),

      body: Center(
        child: RichText(
          text: TextSpan(
            // Creating Default Style
            style: TextStyle(
              color: Colors.blueAccent,
              fontSize: 20,
            ),

            children: <TextSpan>[
              TextSpan(text: 'Hello ',),
              TextSpan(text: 'World,', style: TextStyle(color: Colors.indigo, fontSize: 30, fontWeight: FontWeight.bold)),

              TextSpan(text: " Wellcome to " , style: TextStyle(              fontStyle: FontStyle.italic, color: Colors.grey
              )),
              TextSpan(text: 'Flutter!', style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold, color: Colors.black, fontStyle: FontStyle.italic))
            ]
          ),
        ),
      ),
    );
  }
}
