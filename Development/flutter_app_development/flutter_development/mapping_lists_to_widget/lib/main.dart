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
      home: const MyHomePage(title: 'Mapping Lists To Widget'),
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
  // var arrData = ["", "", "", "", "", "", "", "", "", "Ravi", "Atul", "", "", "", "Md. Israfil", "", "", "", '', ""];
  var arrData = [
    {
      'name': 'Hariom',
      'number': '9876320187',
      'unread': '2'
    },
    {
      'name': 'Shubham',
      'number': '2877566518',
      'unread': '3'
    },
    {
      'name': 'Ankit',
      'number': '9876354286',
      'unread': '6'
    },
    {
      'name': 'Aman',
      'number': '7623456789',
      'unread': '5'
    },
    {
      'name': 'Saket',
      'number': '9898563456',
      'unread': '2'
    },
    {
      'name': 'Aachal',
      'number': '9087987634',
      'unread': '3'
    },
    {
      'name': 'Lokendra',
      'number': '9876231456',
      'unread': '4'
    },
    {
      'name': 'Abhishek',
      'number': '9871234567',
      'unread': '10'
    },
    {
      'name': 'Rupesh',
      'number': '9871234567',
      'unread': '7'
    },
    {
      'name': 'Abhay',
      'number': '9872345678',
      'unread': '1'
    },
    {
      'name': 'Harsh',
      'number': '7890987345',
      'unread': '8'
    },
    {
      'name': 'Akshay',
      'number': '8898763425',
      'unread': '21'
    },
    {
      'name': 'Mehak',
      'number': '7887653213',
      'unread': '2'
    },
    {
      'name': 'Himanshu',
      'number': '9809871247',
      'unread': '12'
    },
    {
      'name': 'Sumit',
      'number': '6776543217',
      'unread': '1'
    },
    {
      'name': 'Ajay',
      'number': '9087908765',
      'unread': '3'
    },
    {
      'name': 'Pradeep',
      'number': '8712456789',
      'unread': '9'
    },
    {
      'name': 'Atul',
      'number': '9988776612',
      'unread': '9'
    },
    {
      'name': 'Ravi',
      'number': '7635412009',
      'unread': '4'
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Container(
          color: Colors.blueGrey.shade100,
          width: double.infinity,
          height: double.infinity,
          child: ListView(
            children: arrData.map((value) {
              // Todo - Common List Style
              return ListTile(
                leading: Icon(Icons.account_circle_sharp, size: 30,),
                title: Text(value['name'].toString()),
                subtitle: Text(value['number'].toString()),
                trailing: CircleAvatar(
                  child: Text(value['unread'].toString()),
                  radius: 10,
                  backgroundColor: Colors.indigo,
                ),
              );
            }).toList()
          ),
        ),
      )
    );
  }
}
