import 'package:curved_labeled_navigation_bar/curved_navigation_bar.dart';
import 'package:curved_labeled_navigation_bar/curved_navigation_bar_item.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'firstPage.dart';

class HomePage extends StatefulWidget{
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _page = 0;
  final List<Widget> screens = [DashBoard()];
  GlobalKey<CurvedNavigationBarState> _bottomNavigationKey = GlobalKey();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueAccent,

      // floatingActionButton: FloatingActionButton(
      //   child: Icon(Icons.sos),
      //   onPressed: () {
      //
      //   },
      // ),

      bottomNavigationBar: CurvedNavigationBar(
        backgroundColor: Colors.blueAccent,
        buttonBackgroundColor: Colors.deepPurpleAccent,
        color: Colors.indigo,
        animationDuration: Duration(milliseconds: 300),
        height: 75,
        // animationCurve: Curves.easeInCirc,

        items: [
          CurvedNavigationBarItem(
            child: Icon(Icons.home_outlined, color: Colors.white,),
            label: 'Home',
            labelStyle: TextStyle(
              color: Colors.white
            )
          ),
          CurvedNavigationBarItem(
            child: Icon(Icons.search, color: Colors.white),
            label: 'Search',
              labelStyle: TextStyle(
                  color: Colors.white
              ),
          ),
          CurvedNavigationBarItem(
            child: Icon(Icons.chat_bubble_outline, color: Colors.white),
            label: 'Chat',
              labelStyle: TextStyle(
                  color: Colors.white
              )
          ),
          CurvedNavigationBarItem(
            child: Icon(Icons.newspaper, color: Colors.white),
            label: 'Feed',
              labelStyle: TextStyle(
                  color: Colors.white
              )
          ),
          CurvedNavigationBarItem(
            child: Icon(Icons.perm_identity, color: Colors.white),
            label: 'Personal',
              labelStyle: TextStyle(
                  color: Colors.white
              )
          ),
        ],

        onTap: (index) {
          setState(() {
            _page = index+1;
          });
        },
      ),
      body: Container(
        color: Colors.blueAccent,
        child: Center(
          child: Column(
            children: <Widget>[

              Padding(
                padding: const EdgeInsets.all(30.0),
                child: Text(_page.toString(), style: TextStyle(
                  color: Colors.white
                ), textScaleFactor: 10.0),
              ),

            ],
          ),
        ),
      ),
      );
  }
}