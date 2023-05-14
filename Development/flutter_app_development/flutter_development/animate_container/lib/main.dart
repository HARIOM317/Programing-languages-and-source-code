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
      home: const MyHomePage(title: 'Animated Container'),
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
  var _width = 300.0;
  var _height = 150.0;
  bool flag = true;

  Decoration myDecoration = BoxDecoration(
    borderRadius: BorderRadius.circular(30),
    color: Colors.indigo,
  );

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
            // Todo - Foo Animations

            // Animated Container
            AnimatedContainer(
              duration: Duration(seconds: 1),
              width: _width,
              height: _height,

              // Todo : Curve define type of animation like easeIn, bounceIn etc using curve graph.
              // curve: Curves.easeIn,
              // curve: Curves.easeInOutSine,
              curve: Curves.easeInOutCubicEmphasized,

              decoration: myDecoration,
            ),

            ElevatedButton(
                onPressed: (){
                  setState(() {
                    if(flag){
                      _width = 300;
                      _height = 150;
                      myDecoration = BoxDecoration(
                        borderRadius: BorderRadius.circular(30),
                        color: Colors.indigo,
                      );
                      flag = false;
                    } else{
                      _width = 150;
                      _height = 300;
                      myDecoration = BoxDecoration(
                        borderRadius: BorderRadius.circular(10),
                        color: Colors.indigoAccent,
                      );
                      flag = true;
                    }
                  });
                },
                child: Text('Animate'),
            )
          ],
        ),
      ),
    );
  }
}
