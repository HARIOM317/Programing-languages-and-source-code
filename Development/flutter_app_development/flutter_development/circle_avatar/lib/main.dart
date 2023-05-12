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
      title: 'Flutter Circular Avatar',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Circular Avatar Demo'),
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
        title: Text("Flutter Circular Avatar"),
      ),

      body: Container(
        margin: EdgeInsets.all(20),
        child: SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          child: Row(
            children: [
              CircleAvatar(
                backgroundImage: AssetImage('assets/images/hariom.jpg'),
                backgroundColor: Colors.transparent,
                radius: 60, // size
                // minRadius: 30,
                // maxRadius: 80,

                child: Text('Hariom', style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 25,
                  fontStyle: FontStyle.italic,
                ),
                ),
              ),

              CircleAvatar(
                backgroundImage: AssetImage('assets/images/1.jpg'),
                backgroundColor: Colors.transparent,
                radius: 60, // size

                child: Text('Car 1', style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 25,
                  fontStyle: FontStyle.italic,
                ),
                ),
              ),

              CircleAvatar(
                backgroundImage: AssetImage('assets/images/2.jpg'),
                backgroundColor: Colors.transparent,
                radius: 60,

                child: Text('Car 2', style: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 25,
                    fontStyle: FontStyle.italic,
                ),
                ),
              ),

              CircleAvatar(
                backgroundImage: AssetImage('assets/images/3.jpg'),
                backgroundColor: Colors.transparent,
                radius: 60,

                child: Text('Car 3', style: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 25,
                    fontStyle: FontStyle.italic,
                ),
                ),
              ),

              CircleAvatar(
                backgroundImage: AssetImage('assets/images/4.jpg'),
                backgroundColor: Colors.transparent,
                radius: 60,

                child: Text('Car 4', style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 25,
                  fontStyle: FontStyle.italic,
                ),
                ),
              ),

              CircleAvatar(
                backgroundImage: AssetImage('assets/images/5.jpg'),
                backgroundColor: Colors.transparent,
                radius: 60,

                child: Text('Car 5', style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 25,
                  fontStyle: FontStyle.italic,
                ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
