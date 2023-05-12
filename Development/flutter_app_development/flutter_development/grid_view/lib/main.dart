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
      title: 'Flutter Scroll View Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
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
  var arrColor = [Colors.yellow, Colors.lightGreenAccent, Colors.greenAccent, Colors.deepPurpleAccent, Colors.red, Colors.indigoAccent, Colors.tealAccent, Colors.blue];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Scroll View"),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            Container(
              height: 200,
              // Todo: <<<GridView with Count>>>
              child: GridView.count(
                crossAxisCount: 4,
                children: [
                  Padding(
                    padding: EdgeInsets.only(left: 5, right: 5, top: 10),
                    child: Container(color: Colors.blueAccent,),
                  ),
                  Padding(
                    padding: EdgeInsets.only(left: 5, right: 5, top: 10),
                    child: Container(color: Colors.lightBlue,),
                  ),
                  Padding(
                    padding: EdgeInsets.only(left: 5, right: 5, top: 10),
                    child: Container(color: Colors.deepPurpleAccent,),
                  ),
                  Padding(
                    padding: EdgeInsets.only(left: 5, right: 5, top: 10),
                    child: Container(color: Colors.red,),
                  ),
                  Padding(
                    padding: EdgeInsets.only(left: 5, right: 5, top: 10),
                    child: Container(color: Colors.orange,),
                  ),
                  Padding(
                    padding: EdgeInsets.only(left: 5, right: 5, top: 10),
                    child: Container(color: Colors.deepOrange,),
                  ),
                  Padding(
                    padding: EdgeInsets.only(left: 5, right: 5, top: 10),
                    child: Container(color: Colors.yellow,),
                  ),
                  Padding(
                    padding: EdgeInsets.only(left: 5, right: 5, top: 10),
                    child: Container(color: Colors.red,),
                  ),
                ],
              ),
            ),

            // Spacing between container
            Container(
              height: 50,
            ),

            Container(
              height: 200,
              // Todo: <<<GridView with extend>>>
              child: GridView.extent(
                maxCrossAxisExtent: 100,
                crossAxisSpacing: 10,
                mainAxisSpacing: 10,
                children: [
                  Container(color: Colors.greenAccent,),
                  Container(color: Colors.green,),
                  Container(color: Colors.lightGreenAccent,),
                  Container(color: Colors.deepPurple,),
                  Container(color: Colors.indigo,),
                  Container(color: Colors.purple,),
                  Container(color: Colors.red,),
                  Container(color: Colors.orange,),
                ],
              ),
            ),

            // Spacing between container
            Container(
              height: 50,
            ),

            Container(
              height: 200,
              // Todo: <<<GridView with builder (It is Dynamic)>>>
              child: GridView.builder(
                itemBuilder: (context, index) {
                  return Container(color: arrColor[index],);
              },
                itemCount: arrColor.length,
                gridDelegate: SliverGridDelegateWithMaxCrossAxisExtent(
                  maxCrossAxisExtent: 100,
                  mainAxisSpacing: 10,
                  crossAxisSpacing: 10,
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
