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
        title: Text("Flutter SizeBox"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // Todo : Button 1
            SizedBox(
              width: 200,
              height: 100,
              child: ElevatedButton(
                style: ButtonStyle(backgroundColor: MaterialStateProperty.resolveWith((states) => Colors.tealAccent)),
                onPressed: () {
                  print("Button 1 Pressed!");
                },
                child: Text('Button 1', style: TextStyle(fontSize: 25, fontWeight: FontWeight.bold),),
              ),
            ),

            SizedBox(height: 20, width: 20,),

            // Todo : Button 2
            SizedBox.square(
              dimension: 150,
              child: ElevatedButton(
                style: ButtonStyle(backgroundColor: MaterialStatePropertyAll<Color>(Colors.lightGreenAccent)),
                onPressed: () {
                  print("Button 2 Pressed!");
                },
                child: Text('Button 2', style: TextStyle(color: Colors.black, fontSize: 30, fontWeight: FontWeight.bold),),
              ),
            ),

            SizedBox(height: 20, width: 20,),

            // Todo : Button 3
            ConstrainedBox(
              constraints: BoxConstraints(
                minWidth: 100,
                minHeight: 40,
                maxWidth: 200,
                maxHeight: 100
              ),
              child: SizedBox.shrink(
                child: ElevatedButton(
                  style: ButtonStyle(backgroundColor: MaterialStateProperty.resolveWith((states) => Colors.indigoAccent)),
                  onPressed: () {
                    print("Button 3 Pressed!");
                  },
                  child: Text('Button 3', style: TextStyle(fontSize: 16),),
                ),
              ),
            ),

            // Todo : Button 4
            SizedBox(height: 20, width: 20,),

            ConstrainedBox(
                constraints: BoxConstraints(
                    minWidth: 100,
                    minHeight: 40,
                    maxWidth: 150,
                    maxHeight: 70
                ),
              child: SizedBox.expand(
                child: ElevatedButton(
                  onPressed: () {
                    print("Button 4 Pressed!");
                  },
                  child: Text('Button 4', style: TextStyle(fontSize: 20),),
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
