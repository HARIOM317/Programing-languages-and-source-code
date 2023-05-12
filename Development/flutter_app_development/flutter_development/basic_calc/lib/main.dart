import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

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
        primarySwatch: Colors.indigo,
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
  var controller1 = TextEditingController();
  var controller2 = TextEditingController();
  var result = "";

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(

        title: Text("Calculator"),
      ),
      body:Container(
        width: double.infinity,
        height: double.infinity,
        color: Colors.indigoAccent.shade100,

        child: Center(
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Padding(
                  padding: const EdgeInsets.only(left: 50, right: 50),
                  child: TextField(
                    keyboardType: TextInputType.number,
                    controller: controller1,
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.only(top: 20, left: 50, right: 50),
                  child: TextField(
                    keyboardType: TextInputType.number,
                    controller: controller2,
                  ),
                ),

                Container(
                  margin: EdgeInsets.only(top: 50, bottom: 50),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      // Todo : Add Button
                      ElevatedButton(
                        onPressed: () {
                          var num1 = int.parse(controller1.text.toString());
                          var num2 = int.parse(controller2.text.toString());

                          var sum = num1+num2;
                          result = "Sum : $sum";
                          setState(() {

                          });
                        },
                        child: FaIcon(FontAwesomeIcons.plus),
                        style: ElevatedButton.styleFrom(
                            padding: EdgeInsets.all(25),
                            shape: CircleBorder(),
                            backgroundColor: Colors.orange,
                            foregroundColor: Colors.white,
                        ),
                      ),

                      // Todo : Subtract Button
                      ElevatedButton(
                        onPressed: () {
                          var num1 = int.parse(controller1.text.toString());
                          var num2 = int.parse(controller2.text.toString());

                          setState(() {
                            var sub = num1-num2;
                            result = "Subtraction : $sub";
                          });
                        },
                        child: FaIcon(FontAwesomeIcons.minus),
                        style: ElevatedButton.styleFrom(
                            padding: EdgeInsets.all(25),
                            shape: CircleBorder(),
                            backgroundColor: Colors.orange,
                            foregroundColor: Colors.white
                        ),
                      ),

                      // Todo : Multiply Button
                      ElevatedButton(
                        onPressed: () {
                          var num1 = int.parse(controller1.text.toString());
                          var num2 = int.parse(controller2.text.toString());

                          setState(() {
                            var product = num1*num2;
                            result = "Product : $product";
                          });
                        },
                        child: FaIcon(FontAwesomeIcons.multiply),
                        style: ElevatedButton.styleFrom(
                            padding: EdgeInsets.all(25),
                            shape: CircleBorder(),
                            backgroundColor: Colors.orange,
                            foregroundColor: Colors.white
                        ),
                      ),

                      // Todo : Divide Button
                      ElevatedButton(
                        onPressed: () {
                          var num1 = int.parse(controller1.text.toString());
                          var num2 = int.parse(controller2.text.toString());

                          var division = num1/num2;
                          result = "Division : ${division.toStringAsFixed(2)}";
                          setState(() {
                          });
                        },
                        child: FaIcon(FontAwesomeIcons.divide),
                        style: ElevatedButton.styleFrom(
                            padding: EdgeInsets.all(25),
                            shape: CircleBorder(),
                            backgroundColor: Colors.orange,
                            foregroundColor: Colors.white
                        ),
                      ),
                    ],
                  ),
                ),

                Padding(
                  padding: const EdgeInsets.only(left: 50, right: 50),
                  child: Text(result, style: TextStyle(
                    fontSize: 30,
                    color: Colors.white,
                    fontWeight: FontWeight.bold
                  ),
                  ),
                )
              ],
            ),
          ),
        ),
        // color: Color("#212121"),
      )
    );
  }
}
