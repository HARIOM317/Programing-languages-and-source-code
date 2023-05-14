import 'dart:async';

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
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Animated Cross Fade Widget'),
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
  bool isFirst = true;

  // @override
  // void initState() {
  //   super.initState();
  //
  //   Timer(Duration(seconds: 3), (){
  //     reload();
  //   });
  // }
  //
  // void reload(){
  //   setState(() {
  //     isFirst = false;
  //   });
  // }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(

        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            AnimatedCrossFade(
              duration: Duration(seconds: 2),
              firstChild: Container(
                width: 250,
                height: 400,
                color: Colors.indigoAccent,

                child: Center(
                  child: Text('Hi, I am HSR', style: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 35
                  ),),
                ),
              ),

              secondChild: Image.asset('assets/images/hariom.jpg', width: 250, height: 400,
              ),

              // sizeCurve: Curves.fastOutSlowIn,  // work on different size

              firstCurve: Curves.fastLinearToSlowEaseIn,
              secondCurve: Curves.easeInOutCubicEmphasized,
              crossFadeState: isFirst ? CrossFadeState.showFirst : CrossFadeState.showSecond,
            ),

            ElevatedButton(
                onPressed: () {
                  if(isFirst){
                    isFirst = false;
                  } else{
                    isFirst = true;
                  }

                  setState(() {

                  });
                },
                child: Text('Switch')
            ),
          ],
        ),
      )
    );
  }
}
