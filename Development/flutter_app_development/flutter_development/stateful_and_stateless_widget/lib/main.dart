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
      title: 'Flutter Stateful Widget Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  // Defining abstract method createState() of class StatefulWidget
  @override
  State<StatefulWidget> createState() {
    return MyHomeState();
  }
}

class MyHomeState extends State<MyHomePage> {
  var count = 0;
  // Defining abstract method build() of class State
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Stateful and Stateless Widget'),
      ),

      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Count : $count', style: TextStyle(fontSize: 60, color: Colors.blueGrey, fontWeight: FontWeight.bold),),
            ElevatedButton(
                onPressed: () {
                  count++;
                  // call setState function to rebuild MyHomeState
                  setState(() {

                  });
                },
                child: Text('Increment Count', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20),),
            ),

            ElevatedButton(
                onPressed: () {
                  count--;

                  setState(() {

                  });
                },
                child: Text('Decrement Count', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20),),
            )
          ],
        ),
      ),
    );
  }
}