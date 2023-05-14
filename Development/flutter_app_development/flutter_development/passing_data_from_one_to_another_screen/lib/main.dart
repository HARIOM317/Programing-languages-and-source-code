import 'package:flutter/material.dart';
import 'package:passing_data_from_one_to_another_screen/profile.dart';

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
      home: MyHomePage(title: "Home Page"),
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
  var nameController = TextEditingController();
  var numberController = TextEditingController();
  var emailController = TextEditingController();
  var professionController = TextEditingController();
  var qualificationController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          children: [
            SizedBox(
              width: 300,
              child: TextField(
                controller: nameController,
                decoration: InputDecoration(
                    hintText: "Enter User name"
                ),
              ),
            ),

            SizedBox(
              width: 300,
              child: TextField(
                controller: numberController,
                decoration: InputDecoration(
                    hintText: "Enter Mobile Number"
                ),
              ),
            ),

            SizedBox(
              width: 300,
              child: TextField(
                controller: emailController,
                decoration: InputDecoration(
                    hintText: "Enter Email"
                ),
              ),
            ),

            SizedBox(
              width: 300,
              child: TextField(
                controller: professionController,
                decoration: InputDecoration(
                    hintText: "Enter Profession"
                ),
              ),
            ),

            SizedBox(
              width: 300,
              child: TextField(
                controller: qualificationController,
                decoration: InputDecoration(
                  hintText: "Enter Qualification"
                ),
              ),
            ),

            Container(
              margin: EdgeInsets.all(20),
              child: ElevatedButton(
                onPressed: () {
                  Navigator.push(context, MaterialPageRoute(builder: (context) => ProfilePage(nameController.text.toString(), numberController.text.toString(), emailController.text.toString(), professionController.text.toString(), qualificationController.text.toString())));
                },
                child: Text('Submit Profile Data'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
