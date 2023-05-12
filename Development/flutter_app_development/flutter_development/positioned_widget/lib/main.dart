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
        primarySwatch: Colors.blueGrey,
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
        title: Text("Flutter Positioned Widget"),
      ),
      body: Center(
        child: Container(
          width: double.infinity,
          height: double.infinity,
          color: Colors.black87,
          child: Stack(
            children: [
              Positioned(
                bottom: 20,
                right: 20,
                child: Container(
                  width: 100,
                  height: 100,
                  color: Colors.white,
                  ),
              ),

              Positioned(
                  bottom: 140,
                  right: 170,
                  child: Container(
                    width: 200,
                    height: 200,
                    color: Colors.white,
                  ),
              ),

              Positioned(
                top: 20,
                right: 10,
                child: Container(
                  width: 300,
                  height: 300,
                  color: Colors.white,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
