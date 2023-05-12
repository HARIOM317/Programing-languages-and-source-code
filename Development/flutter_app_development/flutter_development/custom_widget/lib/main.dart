import 'package:custom_widget/widgets/rounded_button_widget.dart';
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
        primarySwatch: Colors.cyan,
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
        title: Text("My Custom Widget"),
      ),
      body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Todo : Play Button
              Container(
                margin: EdgeInsets.all(10),
                width: 150,
                height: 70,
                child: RoundedButton(
                  buttonName: "Play",
                  icon: Icon(Icons.play_arrow, color: Colors.amberAccent,),
                  callback: (){
                  print("Playing!");
                },
                textStyle: TextStyle(color: Colors.white, fontSize: 20, fontWeight: FontWeight.bold),
                ),
              ),

              // Todo : Pause Button
              Container(
                margin: EdgeInsets.all(10),
                width: 150,
                height: 70,
                child: RoundedButton(
                  buttonName: "Pause",
                  icon: Icon(Icons.pause, color: Colors.amberAccent,),
                  callback: (){
                    print("Paused!");
                  },
                  textStyle: TextStyle(color: Colors.white, fontSize: 20, fontWeight: FontWeight.bold),
                  bgColor: Colors.blueAccent,
                ),
              ),

              // Todo : Stop Button
              Container(
                margin: EdgeInsets.all(10),
                width: 150,
                height: 70,
                child: RoundedButton(
                  buttonName: "Stop",
                  icon: Icon(Icons.stop, color: Colors.amberAccent,),
                  callback: (){
                    print("Stopped!");
                  },
                  textStyle: TextStyle(color: Colors.white, fontSize: 20, fontWeight: FontWeight.bold),
                  bgColor: Colors.blue,
                ),
              ),
            ],
          )
      )
    );
  }
}
