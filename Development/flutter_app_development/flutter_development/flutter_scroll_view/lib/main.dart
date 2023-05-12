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
      title: 'Flutter Scroll View Demo',
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
        title: Text("Scroll View and It's Types"),
      ),
      body: Padding(
        padding: EdgeInsets.all(5.0),

        child: Center(

          // vertically scroll view
          child: SingleChildScrollView(
            child: Column(

              children: [
                // horizontal scroll view
                SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  child: Row(
                    children: [
                      Container(
                        margin: EdgeInsets.only(left: 15),
                        height: 200,
                        width: 170,
                        color: Colors.blue,
                      ),

                      Container(
                        margin: EdgeInsets.only(left: 15),
                        height: 200,
                        width: 170,
                        color: Colors.blue,
                      ),

                      Container(
                        margin: EdgeInsets.only(left: 15),
                        height: 200,
                        width: 170,
                        color: Colors.blue,
                      ),

                      Container(
                        margin: EdgeInsets.only(left: 15),
                        height: 200,
                        width: 170,
                        color: Colors.blue,
                      ),

                      Container(
                        margin: EdgeInsets.only(left: 15, right: 15),
                        height: 200,
                        width: 170,
                        color: Colors.blue,
                      ),
                    ],
                  ),
                ),

                Container(
                  margin: EdgeInsets.all(10),
                  height: 200,
                  width: 350,
                  color: Colors.indigo,
                ),

                Container(
                  margin: EdgeInsets.all(10),
                  height: 200,
                  width: 350,
                  color: Colors.lightBlueAccent,
                ),

                Container(
                  margin: EdgeInsets.all(10),
                  height: 200,
                  width: 350,
                  color: Colors.blueAccent,
                ),

                Container(
                  margin: EdgeInsets.all(10),
                  height: 200,
                  width: 350,
                  color: Colors.indigoAccent,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
