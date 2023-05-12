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
      title: 'Flutter Buttons',
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
        title: Text("Flutter Buttons"),
      ),
      body: Center(
        child: Column(
          children: [
            TextButton(
              child: Text("Text Button"),
              onPressed: (){
               print("Text Button Triggered!");
              },
              onLongPress: (){
                print("Text Button Long Pressed!");
              },
            ),

            ElevatedButton(
              child: Text('Elevated Button'),
              onPressed: (){
                print("Elevated Button Triggered!");
              },
              onLongPress: (){
                print("Elevated Button Long Pressed!");
              },
            ),

            OutlinedButton(
              child: Text('Outlined Button'),
              onPressed: (){
                print("Outlined Button Triggered!");
              },
              onLongPress: (){
                print("Outlined Button Long Pressed!");
              },
            ),
          ],
        ),
      ),
    );
  }
}
