import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:passing_data_from_one_to_another_screen/main.dart';

class ProfilePage extends StatelessWidget{
  var userName;
  var mobileNo;
  var email;
  var profession;
  var qualification;

  ProfilePage(this.userName, this.mobileNo, this.email, this.profession, this.qualification);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("User Profile"),
      ),

      body: Center(
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                margin: EdgeInsets.only(top: 10, left: 50, right: 50),
                height: 100,
                width: double.infinity,
                color: Colors.blue,
                child: Center(
                  child: Text("Name : $userName", style: TextStyle(
                    color: Colors.white,
                    fontSize: 20
                  ),
                  ),
                ),
              ),

              Container(
                margin: EdgeInsets.only(top: 10, left: 50, right: 50),
                height: 100,
                color: Colors.indigoAccent,
                child: Center(
                  child: Text("Number : $mobileNo", style: TextStyle(
                      color: Colors.white,
                      fontSize: 20
                  ),
                  ),
                ),
              ),

              Container(
                margin: EdgeInsets.only(top: 10, left: 50, right: 50),
                height: 100,
                color: Colors.blueAccent,
                child: Center(
                  child: Text("Email : $email", style: TextStyle(
                      color: Colors.white,
                      fontSize: 20
                  ),
                  ),
                ),
              ),

              Container(
                margin: EdgeInsets.only(top: 10, left: 50, right: 50),
                height: 100,
                color: Colors.lightBlue,
                child: Center(
                  child: Text("Profession : $profession", style: TextStyle(
                      color: Colors.white,
                      fontSize: 20
                  ),
                  ),
                ),
              ),

              Container(
                margin: EdgeInsets.only(top: 10, left: 50, right: 50, bottom: 10),
                height: 100,
                color: Colors.blue,
                child: Center(
                  child: Text("Qualification : $qualification", style: TextStyle(
                      color: Colors.white,
                      fontSize: 20
                  ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}