import 'package:flutter/material.dart';
import 'package:style_and_themes/ui_design/util.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Style and Theme Demo',
      debugShowCheckedModeBanner: false,

      theme: ThemeData(
        primarySwatch: Colors.blue,

      //  Global Text Style
        textTheme: TextTheme(

          titleMedium: TextStyle(
            fontSize: 20,
            fontWeight: FontWeight.w300,
            fontStyle: FontStyle.italic,
          ),

            displayLarge: TextStyle(
              fontSize: 25,
              fontWeight: FontWeight.bold,
            ),
        ),
      ),
      home: const MyHomePage(title: 'Flutter Style and Theme Demo'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          children: [
            Text('Dart', style: Theme.of(context).textTheme.displayLarge,),
            Text('Dart is a Programming Language!', style: Theme.of(context).textTheme.titleMedium,),

            // adding additional text style with global text style
            Text('Flutter', style: Theme.of(context).textTheme.displayLarge!.copyWith(color: Colors.lightBlue),),
            Text('Flutter is a Framework!', style: Theme.of(context).textTheme.titleMedium!.copyWith(color: Colors.indigo),),
            // style from other dart file
            Text('Flutter is used to develop cross platform applications.', style: myTextStyle()),
            Text('These was all about color and themes.', style: myTextStyle2(textColor: Colors.green)),
          ],
        ),
      ),
    );
  }
}
