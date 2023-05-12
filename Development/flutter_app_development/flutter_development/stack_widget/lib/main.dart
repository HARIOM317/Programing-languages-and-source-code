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
      title: 'Flutter Stack Widget Demo',
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
        title: Text("Flutter Stack Widget"),
      ),
      body: Center(
        child: Column(
          children: [
            // Todo - Stack 1
            Stack(
              children: [
                Container(
                  width: 250,
                  height: 250,
                  color: Colors.lightBlueAccent,
                ),

                Positioned(
                  top: 40,
                  left: 30,
                  bottom: 20,
                  child: Container(
                    width: 200,
                    height: 200,
                    color: Colors.orange,
                  ),
                ),

                Positioned(
                  top: 50,
                  left: 50,
                  bottom: 50,
                  right: 40,

                  child: Container(
                    width: 120,
                    height: 120,
                    color: Colors.indigoAccent,
                  ),
                ),
              ],
            ),

            // Todo - Stack 2
            Container(
              margin: EdgeInsets.all(30),
              width: 250,
              height: 250,
              child: Stack(
                children: [
                  Container(
                    width: 200,
                    height: 200,
                    color: Colors.black45,
                  ),

                  Positioned(
                    left: 21,
                    top: 21,
                    child: Container(
                      width: 200,
                      height: 200,
                      color: Colors.black38,
                    ),
                  )
                ],
              ),
            )
          ],
        ),
      ),
    );
  }
}
