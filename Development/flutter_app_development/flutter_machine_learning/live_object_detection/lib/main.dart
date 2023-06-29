import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:live_object_detection/homescreen.dart';

List<CameraDescription>? cameras;

Future<Null> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  try {
    cameras = await availableCameras();
  } on CameraException catch (e) {
    print("Error : $e.code \nError message: $e.message");
  }

  runApp(new MainScreen());
}

class MainScreen extends StatelessWidget {
  const MainScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: HomeScreen(cameras!),
    );
  }
}
