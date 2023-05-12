import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class RoundedButton extends StatelessWidget{
  final String buttonName;
  final Icon? icon;
  final Color? bgColor;
  final TextStyle? textStyle;
  final VoidCallback? callback;

  // Constructor
  RoundedButton({
  required this.buttonName,
  this.icon,
  this.bgColor = Colors.indigoAccent,
  this.textStyle,
  this.callback
  });

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
        onPressed: () {
          callback!();
    },
      child: icon != null ? Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          icon!,
          Container(width: 10,),  // for spacing
          Text(buttonName, style: textStyle,)
        ],
      ) : Text(buttonName, style: textStyle,),

      style: ElevatedButton.styleFrom(
        primary: bgColor,
        shadowColor: Colors.black26,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.only(
            topRight: Radius.circular(15),
            bottomLeft: Radius.circular(15)
          )
        )
      ),
    );
  }
}