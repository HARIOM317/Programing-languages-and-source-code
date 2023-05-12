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
        primarySwatch: Colors.blueGrey,
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
        title: Text("Flutter Font Awesome Icons"),
      ),
      body: Center(
        child: Wrap(
          spacing: 30,

          children: [
            FaIcon(FontAwesomeIcons.youtube, size: 50, color: Colors.red,),
            FaIcon(FontAwesomeIcons.amazon, size: 50, color: Colors.amber),
            FaIcon(FontAwesomeIcons.amazonPay, size: 50, color: Colors.blueAccent),
            FaIcon(FontAwesomeIcons.google, size: 50, color: Colors.purpleAccent,),
            FaIcon(FontAwesomeIcons.facebook, size: 50, color: Colors.blueAccent),
            FaIcon(FontAwesomeIcons.linkedin, size: 50, color: Colors.indigo),
            FaIcon(FontAwesomeIcons.github, size: 50,),
            FaIcon(FontAwesomeIcons.twitter, size: 50, color: Colors.lightBlue),
            FaIcon(FontAwesomeIcons.apple, size: 50, color: Colors.grey),
            FaIcon(FontAwesomeIcons.calendar, size: 50, color: Colors.orange),
          ],
        ),
      ),
    );
  }
}
