import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:object_detection/main.dart';
import 'package:tflite/tflite.dart';

class HomePage extends StatefulWidget {
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  bool isWorking = false;
  String result = "";
  late CameraController cameraController;
  CameraImage? imgCamera;

  loadModel() async{
  await Tflite.loadModel(
    model: "assets/mobilenet_v1_1.0_224.tflite",
    labels: "assets/labels.txt",
    numThreads: 1, // defaults to 1
    isAsset: true, // defaults to true, set to false to load resources outside assets
    useGpuDelegate: false // defaults to false, set to true to use GPU delegate
  );
  }

  initCamera(){
    cameraController = CameraController(cameras[0], ResolutionPreset.medium);
    cameraController.initialize().then((value)
    {
      if(!mounted){
        return;
      }

      setState(() {
        cameraController.startImageStream((imageFromStream) => {
          if(!isWorking){
            isWorking = true,
            imgCamera = imageFromStream,
            rumModelOnStreamFrames(),
          }
        });
      });
    });
  }

  rumModelOnStreamFrames() async
  {
    final imgCamera = this.imgCamera;
    if(imgCamera != null){
      var recognitions = await Tflite.runModelOnFrame(
        bytesList: imgCamera.planes.map((plane)
        {
          return plane.bytes;
        }).toList(),

        imageHeight: imgCamera.height,
        imageWidth: imgCamera.width,
        imageMean: 127.5,
        imageStd: 127.5,
        rotation: 90,
        numResults: 2,
        threshold: 0.1,
        asynch: true,
      );
      
      result = "";
      
      recognitions?.forEach((response)
      {
        result += response["label"] + "  " + (response["confidence"] as double).toStringAsFixed(2) + "\n\n";
      });

      setState(() {
        result;
      });

      isWorking = false;
    }
  }

  @override
  void initState() {
    super.initState();

    loadModel();
  }

  @override
  void dispose() async
  {
    super.dispose();

    await Tflite.close();
    cameraController?.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: SafeArea(
        child: Scaffold(
          body: Container(
            decoration: BoxDecoration(
              image: DecorationImage(
                image: AssetImage("assets/jarvis.jpg")
              ),
            ),
            child: Column(
              children: [
                Stack(
                  children: [
                    Center(
                      child: Container(
                        color: Colors.black,
                        height: 320,
                        width: 360,
                        child: Image.asset("assets/camera.jpg"),
                      ),
                    ),
                    Center(
                      child: TextButton(
                        onPressed: (){
                          initCamera();
                        },
                        child: Container(
                          margin: EdgeInsets.only(top: 35),
                          height: 270,
                          width: 360,
                          child: imgCamera == null
                              ? Container(
                            height: 270,
                            width: 360,
                            child: Icon(Icons.photo_camera_front, color: Colors.blueAccent, size: 40,),
                          )
                              : AspectRatio(
                            aspectRatio: cameraController.value.aspectRatio,
                            child: CameraPreview(cameraController),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),

                Center(
                  child: Container(
                    margin: EdgeInsets.only(top: 55.0),
                    child: SingleChildScrollView(
                      child: Text(
                        result,
                        style: TextStyle(
                          backgroundColor: Colors.black87,
                          fontSize: 30.0,
                          color: Colors.white,
                        ),
                        textAlign: TextAlign.center,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
