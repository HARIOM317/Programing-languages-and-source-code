import 'dart:async';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_shared_preferences_login/login_screen.dart';
import 'package:flutter_shared_preferences_login/main.dart';
import 'package:shared_preferences/shared_preferences.dart';

class SplashScreen extends StatefulWidget{
  @override
  State<StatefulWidget> createState() {
    return MySplashScreen();
  }
}

class MySplashScreen extends State<SplashScreen> {
  static const String KEYLOGIN = "Login";

  @override
  void initState() {
    super.initState();

    whereToGo();
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
            child: Text('Welcome to FLUTTER!', style: TextStyle(
                color: Colors.white,
                fontSize: 30,
                fontWeight: FontWeight.bold
            ),),
          ),
        ),
      ),
    );
  }

  void whereToGo() async{
    var sharedPref = await SharedPreferences.getInstance();

    var isLoggedIn = sharedPref.getBool(KEYLOGIN);
    
    Timer(Duration(seconds: 5), (){
      if(isLoggedIn != null){
        if(isLoggedIn == true){
          Navigator.pushReplacement(context, MaterialPageRoute(builder: (context) => MyHomePage(title: "Home Page")));
        } else{
          Navigator.pushReplacement(context, MaterialPageRoute(builder: (context) => LoginPage()));
        }
      } else {
        Navigator.pushReplacement(context, MaterialPageRoute(builder: (context) => LoginPage()));
      }

    });
  }
}