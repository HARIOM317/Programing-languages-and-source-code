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
  var emailText = TextEditingController();
  var passText = TextEditingController();

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        title: Text("User Input in Flutter"),
      ),
      body: Center(
        child: Container(
          width: 300,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                  margin: EdgeInsets.only(top: 10),
                  // TextField 1 for Email
                  child: TextField(
                    keyboardType: TextInputType.emailAddress,
                    controller: emailText,
                    enabled: true,
                    decoration: InputDecoration(
                      hintText: "Enter Email",
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10),
                        borderSide: BorderSide(color: Colors.lightBlue, width: 2,
                        ),
                      ),

                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10),
                        borderSide: BorderSide(color: Colors.grey, width: 1.5,
                        ),
                      ),

                      disabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10),
                        borderSide: BorderSide(color: Colors.grey, width: 1.5),
                      ),

                      prefixIcon: Icon(Icons.email) ,
                    ),
                  ),
                ),

                Container(
                  margin: EdgeInsets.only(top: 10),
                  // TextField 2 for Password
                  child: TextField(
                    keyboardType: TextInputType.number, // change keyboard into number keyboard
                    controller: passText,
                    obscureText: true,  // hide password text
                    decoration: InputDecoration(
                      hintText: "Enter 6 digit Password",
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10),
                        borderSide: BorderSide(color: Colors.lightBlue, width: 2,
                        ),
                      ),

                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10),
                        borderSide: BorderSide(color: Colors.grey, width: 1.5)
                      ),

                      // suffixText: "Wrong exist",
                      suffixIcon: IconButton(
                        icon: Icon(Icons.remove_red_eye, color: Colors.deepPurpleAccent,),
                        onPressed: (){
                          print("Button Pressed!");
                        },
                      ),
                      prefixIcon: Icon(Icons.lock),

                    ),
                  ),
                ),

                ElevatedButton(onPressed: (){
                  String userEmail = emailText.text.toString();
                  String userPass = passText.text.toString();

                  print("Email : $userEmail\nPassword : $userPass");
                }, child: Text("Submit"))
              ],
            ),
        ),
      ),
    );
  }
}
