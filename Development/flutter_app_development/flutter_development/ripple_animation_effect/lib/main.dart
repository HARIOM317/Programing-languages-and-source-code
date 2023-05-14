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
      home: const MyHomePage(title: 'Flutter Ripple Animation Effect'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> with SingleTickerProviderStateMixin{
  late Animation _animation;
  late AnimationController _animationController;

  var listRadius = [150.0, 200.0, 250.0, 300.0, 350.0];

  @override
  void initState() {
    // TODO: implement initState
    super.initState();

    _animationController = AnimationController(vsync: this, duration: Duration(seconds: 4), lowerBound: 0.5);

    // <<<  With _animation >>>
    // _animation = Tween(begin: 0.0, end: 1.0).animate(_animationController);
    
    _animationController.addListener(() {
      setState(() {

      });
    });

    _animationController.forward();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Stack(
          alignment: Alignment.center,
          children: [
            // Todo : Creating Container Widget using a function
            buildMyContainer(listRadius[0]),
            buildMyContainer(listRadius[1]),
            buildMyContainer(listRadius[2]),
            buildMyContainer(listRadius[3]),
            buildMyContainer(listRadius[4]),
            
            Icon(Icons.add_call, size: 50,),
          ]
        ),
      )
    );
  }

  // function to create Container widget
Widget buildMyContainer (radius) {
    return Container(
      // <<<  With _animation >>>
      // width: radius*_animation.value,
      // height: radius*_animation.value,

      // <<<  With _animationController >>>
      width: radius*_animationController.value,
      height: radius*_animationController.value,
      decoration: BoxDecoration(
        shape: BoxShape.circle,

        // <<<  With _animation >>>
        // color: Colors.indigoAccent.withOpacity(1.0 - _animation.value),

        // <<<  With _animationController >>>
        color: Colors.lightBlueAccent.withOpacity(1.0 - _animationController.value),
      ),
    );
}
}
