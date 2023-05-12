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
      title: 'Flutter Demo Ink Well Widget',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blueGrey,
      ),
      home: const MyHomePage(title: 'Flutter Demo InkWell Widget'),
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
        title: Text("Flutter InkWell Widget"),
      ),
      body: Center(
        child: InkWell(
          onTap: (){
            print("One Tap on Container!");
          },
          onLongPress: (){
            print("Long Press on Container!");
          },
          onDoubleTap: (){
            print("Double Tap on Container!");
          },

          child: Container(
            width: 250,
            height: 200,
            color: Colors.tealAccent,

            child: Center(
                child: InkWell(
                  onTap: (){
                    print("Hey, you just triggered the text inside container!");
                  },
                  onDoubleTap: (){
                    print("Hey, you just double tap the text inside container!");
                  },

                  child: Text("CLICK on this Container!", style: TextStyle(
                    color: Colors.white,
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                  ),
                )
            ),
          ),
        ),
      ),
    );
  }
}
