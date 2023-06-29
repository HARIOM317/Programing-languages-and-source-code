// @dart=2.19.6
import 'package:flutter/material.dart';
import 'package:object_detection/HomePage.dart';
import 'package:splashscreen/splashscreen.dart';

class MySplashPage extends StatefulWidget {
  const MySplashPage({Key? key}) : super(key: key);

  @override
  State<MySplashPage> createState() => _MySplashPageState();
}

class _MySplashPageState extends State<MySplashPage> {
  @override
  Widget build(BuildContext context) {
    return SplashScreen(
      seconds: 5,
      navigateAfterSeconds: HomePage(),
      imageBackground: Image.asset("assets/back.jpg").image,
      useLoader: true,
      loaderColor: Colors.amber,
      loadingText: Text("Loading...", style: TextStyle(color: Colors.white),),
    );
  }
}
