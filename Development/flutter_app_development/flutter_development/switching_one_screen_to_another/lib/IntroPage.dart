import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:switching_one_screen_to_another/main.dart';

class IntroPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Introduction"),
      ),

      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Hello, I am HSR', style: TextStyle(
              fontSize: 30,
              fontWeight: FontWeight.bold,
              color: Colors.indigoAccent
            ),
            ),

            SizedBox(height: 20,),

            ElevatedButton(
                onPressed: () {
                  Navigator.push(context,
                    MaterialPageRoute(builder: (context) => MyHomePage(title: "Home Page"),),
                  );
                },
                child: Text('Next'),
            )
          ],
        ),
      ),
    );
  }
}