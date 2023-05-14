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
        primarySwatch: Colors.indigo,
      ),
      home: const MyHomePage(title: 'BMI Calculator'),
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
  // required variables
  var weightController = TextEditingController();
  var feetController = TextEditingController();
  var inchController = TextEditingController();

  var msg = "";
  var result = "";
  var bgColor = Colors.indigo.shade200;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(

        title: Text(widget.title),
      ),

      body: Container(
        color: bgColor,
        child: Center(
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                // Todo: BMI Text
                Container(
                  margin: EdgeInsets.all(20),
                  child: Text('BMI', style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 50,
                    color: Colors.indigoAccent
                  ),
                  ),
                ),

                // Todo: TextField for Weight
                Container(
                  width: 300,
                  margin: EdgeInsets.all(15),
                  child: TextField(
                    controller: weightController,
                    decoration: InputDecoration(
                      label: Text("Enter Weight (In Kg)"),
                      prefixIcon: Icon(Icons.line_weight, size: 50,),
                    ),
                    keyboardType: TextInputType.number
                  ),
                ),

                // Todo: TextField for Height
                Container(
                  width: 300,
                  margin: EdgeInsets.all(15),
                  child: TextField(
                      controller: feetController,
                      decoration: InputDecoration(
                        label: Text("Enter Height (In Feet)"),
                        prefixIcon: Icon(Icons.height, size: 50,),
                      ),
                      keyboardType: TextInputType.number
                  ),
                ),

                // Todo: TextField for Length
                Container(
                  width: 300,
                  margin: EdgeInsets.all(15),
                  child: TextField(
                      controller: inchController,
                      decoration: InputDecoration(
                        label: Text("Enter Length (In Inch)"),
                        prefixIcon: Icon(Icons.hail_outlined, size: 50,),
                      ),
                      keyboardType: TextInputType.number
                  ),
                ),

                // Todo: Button and Logic part
                Container(
                  margin: EdgeInsets.all(15),
                  child: ElevatedButton(
                      onPressed: () {
                        var weight = weightController.text.toString();
                        var feet = feetController.text.toString();
                        var inch = inchController.text.toString();

                        if(weight != "" && feet != "" && inch != ""){
                          //  BMI Calculation
                          var wt = int.parse(weight);
                          var ft = int.parse(feet);
                          var ich = int.parse(inch);

                          var totalInches = (ft*12) + ich;
                          var totalCm = totalInches * 2.54;
                          var totalMeter = totalCm/100;

                          var bmi = wt/(totalMeter*totalMeter);

                          // logic to change bg color
                          if(bmi > 25){
                            msg = "You are OverWeight!!";
                            bgColor = Colors.orange.shade200;
                          } else if(bmi < 18){
                            msg = "You are UnderWeight!!";
                            bgColor = Colors.red.shade200;
                          } else {
                            msg = "You are Healthy!";
                            bgColor = Colors.green.shade200;
                          }

                          setState(() {
                            result = "Your BMI = ${bmi.toStringAsFixed(2)}";
                          });

                        } else {
                          setState(() {
                            result = "Please fill all the required fields!";
                            msg = "";
                            bgColor = Colors.indigo.shade200;
                          });
                        }
                      },
                      child: Text('Calcutale'),
                  ),
                ),

                // Todo: result
                Container(
                  margin: EdgeInsets.only(top: 15, bottom: 10),
                  child: Text(result, style: TextStyle(
                    fontSize: 25,
                    fontWeight: FontWeight.bold
                  ),
                  ),
                ),

                // Todo: Message
                Text(msg, style: TextStyle(
                    fontSize: 20,
                  color: Colors.black87
                ),
                )
              ],
            ),
          ),

        ),
      ),
    );
  }
}
