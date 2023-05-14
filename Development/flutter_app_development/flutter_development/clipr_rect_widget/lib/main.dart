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
        primarySwatch: Colors.blueGrey,
      ),
      home: const MyHomePage(title: 'Flutter ClipRRect Widget'),
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
        title: Text(widget.title),
      ),
      body: Container(
        padding: EdgeInsets.only(top: 20, bottom: 20),
        width: double.infinity,
        height: double.infinity,
        color: Colors.grey.shade300,

        child: Center(
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [

                // Todo - For Container 1
                ClipRRect(
                  borderRadius: BorderRadius.only(topLeft: Radius.elliptical(70, 20), bottomRight: Radius.circular(50)),
                  child: Container(
                    // margin: EdgeInsets.all(30),
                    color: Colors.blueAccent,
                    width: 300,
                    height: 150,

                    child: Center(child: Text("HELLO", style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 40),)),
                  ),
                ),

                // Todo - For Image
                Padding(
                  padding: const EdgeInsets.all(25.0),
                  child: ClipRRect(
                    borderRadius: BorderRadius.only(topLeft: Radius.circular(60), topRight: Radius.circular(20), bottomLeft: Radius.circular(20)),
                    child: Image.asset('assets/images/flower.jpg', width: 300,),
                  ),
                ),

                // Todo - For Image 2
                ClipRRect(
                  borderRadius: BorderRadius.circular(100),
                  child: Container(
                    width: 200,
                    height: 200,
                    color: Colors.indigoAccent,

                    child: Center(
                      child: Text("WORLD", style: TextStyle(
                        fontSize: 40, fontWeight: FontWeight.bold, color: Colors.white
                      ),),
                    ),
                  ),
                )
              ],
            ),
          )
          ),
      ),
    );
  }
}
