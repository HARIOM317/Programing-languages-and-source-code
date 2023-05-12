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
        title: Text("Wrap Widget"),
      ),

      body: Center(
        child: Wrap(
          direction: Axis.horizontal,
          spacing: 10,
          runSpacing: 10,
          alignment: WrapAlignment.center,

          children: [
            Container(width: 95, height: 100, color: Colors.red,),
            Container(width: 95, height: 100, color: Colors.blue,),
            Container(width: 95, height: 100, color: Colors.purple,),
            Container(width: 95, height: 100, color: Colors.pink,),
            Container(width: 95, height: 100, color: Colors.yellow,),
            Container(width: 95, height: 100, color: Colors.green,),
            Container(width: 95, height: 100, color: Colors.indigo,),
            Container(width: 95, height: 100, color: Colors.blueAccent,),
            Container(width: 95, height: 100, color: Colors.orangeAccent,),
            Container(width: 95, height: 100, color: Colors.indigoAccent,),
          ],
        ),
      ),
    );
  }
}
