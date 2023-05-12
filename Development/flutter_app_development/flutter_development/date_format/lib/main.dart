import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Date Format Demo',
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
    var time = DateTime.now();
    
    return Scaffold(
      appBar: AppBar(

        title: Text("date Formating"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("Current Time : ${DateFormat('jms').format(time)}", style: TextStyle(color: Colors.lightBlue, fontStyle: FontStyle.italic, fontSize: 20),),

            Text("Current Time : ${DateFormat('Hms').format(time)}", style: TextStyle(color: Colors.indigoAccent, fontStyle: FontStyle.italic, fontSize: 20),),

            Text("Current Time : ${DateFormat('yMMMMd').format(time)}", style: TextStyle(color: Colors.red, fontStyle: FontStyle.italic, fontSize: 20),),

            Text("Current Time : ${DateFormat('jm').format(time)}", style: TextStyle(color: Colors.green, fontStyle: FontStyle.italic, fontSize: 20),),

            Text("Current Time : ${DateFormat('Hm').format(time)}", style: TextStyle(color: Colors.blueAccent, fontStyle: FontStyle.italic, fontSize: 20),),

            Text("Current Time : ${DateFormat('yMMMMEEEEd').format(time)}", style: TextStyle(color: Colors.cyan, fontStyle: FontStyle.italic, fontSize: 20),),
          ],
        ),
      ),
    );
  }
}
