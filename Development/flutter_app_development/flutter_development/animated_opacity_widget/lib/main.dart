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
      home: const MyHomePage(title: 'Flutter Animated Opacity Widget'),
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
  var myOpacity = 1.0;
  var buttonText = "Hide";
  bool flag = true;
  bool flag2 = true;

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
            AnimatedOpacity(
              opacity: myOpacity,
              duration: Duration(seconds: 3),
              curve: Curves.easeOutQuart,

              child: Container(
                width: 300,
                height: 200,
                color: Colors.indigo,
              ),
            ),

            Container(
              width: 150,
              height: 40,
              margin: EdgeInsets.all(50),
              child: ElevatedButton(
                  onPressed: (){
                    setState(() {
                      if(flag){
                        myOpacity = 1.0;
                        buttonText = "Reduce Opacity";
                        flag = false;
                      } else if(flag2){
                        myOpacity = 0.5;
                        buttonText = "Hide";
                        flag2 = false;
                      } else{
                        myOpacity = 0.0;
                        buttonText = "Show";
                        flag = true;
                        flag2 = true;
                      }
                    });
                  },
                  child: Text(buttonText),
              ),
            ),
          ],
        ),
      )
    );
  }
}
