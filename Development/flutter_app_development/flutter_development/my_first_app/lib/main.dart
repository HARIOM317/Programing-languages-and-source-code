import 'package:flutter/material.dart';
import 'dart:ui';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // const MyApp({Key key}) : super(Key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.blueAccent,
        body: Container(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              CircleAvatar(
                radius: 50.0,
                backgroundImage: AssetImage('images/hsr.jpg'),
              ),
              Text(
                'Hariom Singh Rajput',
                style: TextStyle(
                  fontFamily: 'Pacifico',
                  fontSize: 30.0,
                  fontWeight: FontWeight.bold,
                  letterSpacing: 2.0,
                  color: Colors.white,
                ),
              ),
              Text(
                'Flutter Developer',
                style: TextStyle(
                  fontSize: 20.0,
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  letterSpacing: 2.0,
                ),
              ),
              Card(
                color: Colors.white,
                margin: EdgeInsets.symmetric(
                  vertical: 10.0,
                  horizontal: 25.0,
                ),
                child: ListTile(
                  leading: Icon(
                    Icons.phone,
                    color: Colors.lightBlueAccent,
                  ),
                  title: Text(
                    '+91 9302765839',
                    style: TextStyle(
                        fontSize: 15.0,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 1.0,
                        color: Colors.lightBlueAccent),
                  ),
                ),
              ),
              Card(
                color: Colors.white,
                margin: EdgeInsets.symmetric(
                  vertical: 10.0,
                  horizontal: 25.0,
                ),
                child: ListTile(
                  leading: Icon(
                    Icons.email,
                    color: Colors.lightBlueAccent,
                  ),
                  title: Text(
                    'hariommewada484@gmail.com',
                    style: TextStyle(
                        color: Colors.lightBlueAccent,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 1.0,
                        fontSize: 15.0),
                  ),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
