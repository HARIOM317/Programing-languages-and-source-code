import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:google_nav_bar/google_nav_bar.dart';

class HomePage extends StatefulWidget{
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () {

        },
      ),

      bottomNavigationBar: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(colors: [Colors.lightBlueAccent, Colors.blueAccent])

        ),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 15.0, vertical: 20),
          child: GNav(
          tabBackgroundGradient: LinearGradient(colors: [Colors.indigo, Colors.indigoAccent]),
          color: Colors.white,
          activeColor: Colors.white,
          tabBackgroundColor: Colors.grey.shade800,
          gap: 0,

          onTabChange: (index){
            print(index);
          },

          padding: EdgeInsets.only(top: 8, bottom: 8, left: 5, right: 5),
          tabs: const [
              GButton(
                icon: Icons.home,
                text: 'Home',
              ),
              GButton(
                icon: Icons.person_add,
                text: 'Network',
              ),
              GButton(
                icon: Icons.contacts,
                text: 'Contact',
              ),
              GButton(
                icon: Icons.chat_sharp,
                text: 'Chat',
              ),
              GButton(
                icon: Icons.person,
                text: 'Profile',
              ),
            ],
        ),
        ),
      )
    );
  }
}