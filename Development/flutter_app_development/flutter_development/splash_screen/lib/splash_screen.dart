import 'dart:async';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:splash_screen/main.dart';

class SplashScreen extends StatefulWidget{
  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();

    Timer(Duration(seconds: 5), (){
      Navigator.pushReplacement(context, MaterialPageRoute(builder: (context) => MyHomePage(title: "Splash Screen Demo")));
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
          width: double.infinity,
          height: double.infinity,
          color: Colors.blue.shade500,
          child: Center(
            child: Text(
              'Welcome to FLUTTER!',
              style: TextStyle(
                color: Colors.white,
                fontSize: 30,
                fontWeight: FontWeight.bold
              ),
            ),
          ),
        ),
      ),
    );
  }
}