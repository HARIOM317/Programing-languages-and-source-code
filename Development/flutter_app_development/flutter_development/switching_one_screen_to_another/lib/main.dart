import 'package:flutter/material.dart';
import 'package:switching_one_screen_to_another/IntroPage.dart';

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
      home: IntroPage(),
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

        title: Text("Home Page"),
      ),
      body: Center(
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(padding: EdgeInsets.all(10), margin: EdgeInsets.only(top: 10, bottom: 10, left: 50, right: 50) , height: 100, color: Colors.indigoAccent,),
              Container(padding: EdgeInsets.all(10), margin: EdgeInsets.only(top: 10, bottom: 10, left: 50, right: 50) , height: 100, color: Colors.indigoAccent,),
              Container(padding: EdgeInsets.all(10), margin: EdgeInsets.only(top: 10, bottom: 10, left: 50, right: 50) , height: 100, color: Colors.indigoAccent,),
              Container(padding: EdgeInsets.all(10), margin: EdgeInsets.only(top: 10, bottom: 10, left: 50, right: 50) , height: 100, color: Colors.indigoAccent,),
              Container(padding: EdgeInsets.all(10), margin: EdgeInsets.only(top: 10, bottom: 10, left: 50, right: 50) , height: 100, color: Colors.indigoAccent,),
            ],
          ),
        ),
      ),
    );
  }
}
