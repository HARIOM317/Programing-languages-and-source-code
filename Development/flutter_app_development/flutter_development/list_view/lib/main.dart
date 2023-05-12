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
      home: const MyHomePage(title: 'Flutter List View Demo'),
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

    // Array ListView.builder (Dynamic List)
    var programmingLanguages = ["C Language", "C++ Language", "Java Language", "Python Language", "JavaScript Language", "Dart Language", "Kotlin Language", "R Language", "Swift Language", "C# Language"];

    // Array
    var development = ["APP Development", "Web Development", "Frontend Development", "Backend Development", "Machine Learning", "Data Science", "Block Chain Development"];

    return Scaffold(
      appBar: AppBar(
        title: Text("List View"),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Container(
              height: 250,
              child: new Flexible(

                // Static List View
                child: ListView(
                scrollDirection: Axis.vertical,
                reverse: false,

                children: [
                  Container(
                    margin: EdgeInsets.only(left: 10, right: 10, top: 5, bottom: 5),
                    color: Colors.indigoAccent,
                    height: 100,
                    child: Center(
                        child: Text("Hariom Singh Rajput", style: TextStyle(color: Colors.white, fontSize: 25),),
                    ),
                  ),

                  Container(
                    margin: EdgeInsets.only(left: 10, right: 10, bottom: 5),
                    color: Colors.indigo,
                    height: 100,
                    child: Center(
                      child: Text("Abhishek Mewada", style: TextStyle(color: Colors.white, fontSize: 25),),
                    ),
                  ),

                  Container(
                    margin: EdgeInsets.only(left: 10, right: 10, bottom: 5),
                    color: Colors.indigoAccent,
                    height: 100,
                    child: Center(
                      child: Text("Sumit Kumar", style: TextStyle(color: Colors.white, fontSize: 25),),
                    ),
                  ),

                  Container(
                    margin: EdgeInsets.only(left: 10, right: 10, bottom: 5),
                    color: Colors.indigo,
                    height: 100,
                    child: Center(
                      child: Text("Himanshu Nagose", style: TextStyle(color: Colors.white, fontSize: 25),),
                    ),
                  ),

                  Container(
                    margin: EdgeInsets.only(left: 10, right: 10, bottom: 5),
                    color: Colors.indigoAccent,
                    height: 100,
                    child: Center(
                      child: Text("Rupesh", style: TextStyle(color: Colors.white, fontSize: 25),),
                    ),
                  ),
                ],
              ),
              ),
            ),


            Container(
              height: 250,
              margin: EdgeInsets.only(top: 50),
              child: new Flexible(

                  // Dynamic List View
                  child: ListView.builder(itemBuilder: (context, index){
                    return Container(
                        color: Colors.lightBlue,
                        margin: EdgeInsets.only(left: 10, right: 10),
                        padding: EdgeInsets.all(10),
                        child: Center(
                          child: Text(programmingLanguages[index], style: TextStyle(
                              fontSize: 25,
                              color: Colors.black
                          ),
                          ),
                        ),
                    );
                  },
                    itemCount: programmingLanguages.length,
                    itemExtent: 70,
                  ),
              ),
            ),


            Container(
              height: 250,
              margin: EdgeInsets.only(top: 50),
              child: Flexible(

                // Dynamic List View
                child: ListView.separated(itemBuilder: (context, index){
                  return Container(
                    color: Colors.tealAccent,
                    margin: EdgeInsets.only(left: 10, right: 10),
                    padding: EdgeInsets.all(15),

                    child: Center(
                      child: Text(development[index], style: TextStyle(
                          fontSize: 25,
                          color: Colors.black
                      ),
                      ),
                    ),
                  );
                },
                    itemCount: development.length,
                    separatorBuilder: (context, index){
                    return Divider(height: 1, thickness: 4);
                  }
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
