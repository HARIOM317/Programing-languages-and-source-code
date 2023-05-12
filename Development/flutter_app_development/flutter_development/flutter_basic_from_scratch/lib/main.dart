import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
void main(){
  // calling MyFlutterFirstApp class
  runApp(MyFlutterFirstApp());
}

// extends either StatelessWidget (no any changes reflect in runtime in app UI) or StatefulWidget (for runtime changes in UI)
class MyFlutterFirstApp extends StatelessWidget {
  // Defining build() abstract method of StatelessWidget class
  @override
  Widget build(BuildContext context){
    // retuning an UI Type like CupertinoApp, MaterialApp etc.
    return MaterialApp(
      // app title
      title: "My First Flutter Application",
      // removing debug banner
      debugShowCheckedModeBanner: false,

      theme: ThemeData(
        primarySwatch: Colors.blue
      ),
      home: MyHomePageScreen(),
    );
  }
}

// extends either StatelessWidget (no any changes reflect in runtime in UI) or StatefulWidget (for runtime changes in UI)
class MyHomePageScreen extends StatelessWidget{
  // Defining build() abstract method of StatelessWidget class
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // creating appbar
      appBar: AppBar(
        // appbar title
        title: Text('My First App HomePage'),
      ),

      //  creating app body
      body: Center(
        child: Container(
          color: Colors.indigoAccent,
          height: 200,
          width: 300,

          child: Center(child: Text("HELLO WORLD", style: TextStyle(fontWeight: FontWeight.bold, fontSize: 30, color: Colors.white),)),
        ),
      ),
    );
  }
}