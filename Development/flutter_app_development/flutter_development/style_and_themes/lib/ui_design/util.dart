
import 'dart:ui';
import 'package:flutter/material.dart';

TextStyle myTextStyle(){
  return TextStyle(
    fontSize: 15,
    fontWeight: FontWeight.bold,
    fontStyle: FontStyle.italic,
    color: Colors.red,
  );
}
TextStyle myTextStyle2({Color textColor=Colors.deepOrangeAccent, FontWeight fontWeight=FontWeight.w500}){
  return TextStyle(
    fontSize: 20,
    fontWeight: fontWeight,
    fontStyle: FontStyle.italic,
    color: textColor,
  );
}