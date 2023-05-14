import 'package:flutter/material.dart';
import 'package:flutter_shared_preferences_login/login_screen.dart';
import 'package:flutter_shared_preferences_login/my_splash_screen.dart';
import 'package:shared_preferences/shared_preferences.dart';

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
      home: SplashScreen(),
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
        title: Text("Home Page"),
      ),
      body: Center(
        child: Container(
          width: double.infinity,
          height: double.infinity,
          color: Colors.blue.shade100,
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(Icons.home_filled, size: 100, color: Colors.indigoAccent,
                ),

                createContainer(Colors.blueAccent),
                createContainer(Colors.blue),
                createContainer(Colors.lightBlue),

                ElevatedButton(
                    onPressed: () async{
                      var sharedPref = await SharedPreferences.getInstance();
                      sharedPref.setBool(MySplashScreen.KEYLOGIN, false);

                      Navigator.pushReplacement(context, MaterialPageRoute(builder: (context) => LoginPage()));
                    },
                    child: Text('Log Out')
                )
              ],
            ),
          ),
        ),
      ),
    );
  }

  Container createContainer(color){
    return Container(
      width: double.infinity,
      height: 150,
      margin: EdgeInsets.only(top: 5, bottom: 10, left: 30, right: 30),
      padding: EdgeInsets.all(10),

      decoration: BoxDecoration(
          color: color,
          borderRadius: BorderRadius.circular(20.0)
      ),
    );
  }
}
