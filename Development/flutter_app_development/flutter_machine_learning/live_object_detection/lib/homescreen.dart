// import 'package:camera/camera.dart';
// import 'package:flutter/cupertino.dart';
// import 'package:flutter/material.dart';
// import 'package:tflite/tflite.dart';

// const String ssd = "SSD MobileNet";

// class HomeScreen extends StatefulWidget {
//   final List<CameraDescription> cameras;

//   HomeScreen(this.cameras);

//   @override
//   State<HomeScreen> createState() => _HomeScreenState();
// }

// class _HomeScreenState extends State<HomeScreen> {
//   List<dynamic>? _recognitions;
//   int _imageHeight = 0;
//   int _imageWidth = 0;
//   String _model = "";

// loadModel() async {
//   String? result;

//   switch (_model) {
//     case ssd:
//       result = await Tflite.loadModel(
//           labels: "assets/models/labels.txt",
//           model: "assets/models/ssd_mobilenet.tflite");
//   }
// }

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: _model == ""
//           ? Container()
//           : Stack(
//               children: [],
//             ),
//       floatingActionButton: FloatingActionButton(
//         onPressed: () {},
//         child: Icon(Icons.photo_camera),
//       ),
//     );
//   }
// }

import 'package:camera/camera.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:live_object_detection/camera.dart';
import 'package:tflite/tflite.dart';

// import 'package:camera/camera.dart';
// import 'package:camera/new/src/support_android/camera.dart';
// import 'package:flutter/material.dart';
import 'package:live_object_detection/boundingBox.dart';
// import 'package:tflite/tflite.dart';
import 'dart:math' as math;

const String ssd = "SSD MobileNet";

class HomeScreen extends StatefulWidget {
  final List<CameraDescription> cameras;

  HomeScreen(this.cameras);

  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  List<dynamic>? _recognitions;
  int _imageHeight = 0;
  int _imageWidth = 0;
  String _model = "";

  loadModel() async {
    String? result;

    switch (_model) {
      case ssd:
        result = await Tflite.loadModel(
            labels: "assets/models/labels.txt",
            model: "assets/models/ssd_mobilenet.tflite");
    }
  }

  onSelectModel(model) {
    setState(() {
      _model = model;
    });

    loadModel();
  }

  setRecognitions(recognitions, imageHeight, imageWidth) {
    setState(() {
      _recognitions = recognitions;
      _imageHeight = imageHeight;
      _imageWidth = imageWidth;
    });
  }

  @override
  Widget build(BuildContext context) {
    Size screen = MediaQuery.of(context).size;
    return Scaffold(
      body: _model == ""
          ? Container()
          : Stack(
              children: [
                Camera(widget.cameras, _model, setRecognitions),
                BoundingBox(
                    _recognitions ?? [],
                    math.max(_imageHeight, _imageWidth),
                    math.min(_imageHeight, _imageWidth),
                    screen.width,
                    screen.height,
                    _model)
              ],
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          onSelectModel(ssd);
        },
        child: Icon(Icons.photo_camera),
      ),
    );
  }
}
