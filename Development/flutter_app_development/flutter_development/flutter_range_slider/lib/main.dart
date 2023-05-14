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
      home: const MyHomePage(title: 'Flutter Range Slider'),
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
  // Slider Value Range
  RangeValues values = RangeValues(0, 100);

  @override
  Widget build(BuildContext context) {
    // Slider Label
    RangeLabels labels = RangeLabels(values.start.toString(), values.end.toString());

    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // Range Slider
            RangeSlider(
                values: values,
                labels: labels,
                min: 0,
                max: 100,
                divisions: 20,
                activeColor: Colors.indigo,
                inactiveColor: Colors.blueGrey.shade300,
                onChanged: (newValue) {
                  setState(() {
                    values = newValue;
                  });
                },
            ),

            Container(
              margin: EdgeInsets.only(top: 50),
              child: Center(
                child: Text('Starting Value: ${values.start}', style: TextStyle(
                  fontSize: 25,
                  fontWeight: FontWeight.bold
                ),),
              ),
            ),

            Container(
              margin: EdgeInsets.all(20),
              child: Center(
                child: Text('Ending Value: ${values.end}', style: TextStyle(
                    fontSize: 25,
                    fontWeight: FontWeight.bold
                ),),
              ),
            )
          ],
        ),
      ),
    );
  }
}
