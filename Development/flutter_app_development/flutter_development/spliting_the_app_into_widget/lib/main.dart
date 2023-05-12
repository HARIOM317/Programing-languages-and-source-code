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
        title: Text("Spliting the app into widgets"),
      ),
      body: Column(
        children: [
          CatItems(),
          Contacts(),
          SubCatItems(),
          BottomMenu()
        ],
      ),
    );
  }
}

// Todo : Section 1 of Layout
class CatItems extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return  Expanded(
        flex: 4,
        child: Container(
          height: 150,
          color: Colors.blueGrey,
          child: ListView.builder(itemBuilder: (context, index) => Padding(
            padding: const EdgeInsets.all(10.0),
            child: SizedBox(
              width: 150,
              child: CircleAvatar(
                backgroundColor: Colors.greenAccent,
              ),
            ),
          ),
            itemCount: 10,
            scrollDirection: Axis.horizontal,
          ),
        )
    );
  }
}

// Todo : Section 2 of Layout
class Contacts extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Expanded(
        flex: 6,
        child: Container(
          color: Colors.black26,
          child: ListView.builder(itemBuilder: (context, index) => Padding(
            padding: const EdgeInsets.all(8.0),
            child: ListTile(
              leading: CircleAvatar(backgroundColor: Colors.white,),
              title: Text('Name', style: TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text('Mobile No'),
              trailing: Icon(Icons.delete, color: Colors.white,),
            ),
          ),
            itemCount: 10,
          ),
        )
    );
  }
}

// Todo : Section 3 of Layout
class SubCatItems extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Expanded(
        flex: 3,
        child: Container(
          color: Colors.lightGreenAccent,
          child: ListView.builder(itemBuilder: (context, index) =>
              Padding(
                padding: EdgeInsets.all(8.0),
                child: Container(
                  width: 200,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(10),
                    color: Colors.blue,
                  ),
                ),
              ),
            itemCount: 10,
            scrollDirection: Axis.horizontal,
          ),
        )
    );
  }
}

// Todo : Section 4 of Layout
class BottomMenu extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Expanded(
        flex:2,
        child: Container(
          color: Colors.lightBlueAccent,
          child: ListView.builder(itemBuilder: (context, index) =>
              Padding(
                padding: EdgeInsets.all(8.0),
                child: Container(
                  width: 100,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(10),
                    color: Colors.orange,
                  ),
                ),
              ),
            itemCount: 10,
            scrollDirection: Axis.horizontal,
          ),
        )
    );
  }
}
