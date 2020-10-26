import 'package:flutter/material.dart';

class IntroView1 extends StatelessWidget {

  final double space;
  
  IntroView1(this.space);


  @override
  Widget build(BuildContext context) {
    final width =  MediaQuery.of(context).size.width;
    final height = MediaQuery.of(context).size.height;
    final titleTextStyle = TextStyle(fontSize: 20, fontWeight: FontWeight.w800, color: Color(0xCC7442F0));
    final subTitleTextStyle = TextStyle(fontSize: 27, fontWeight: FontWeight.w800, color: Colors.black);

    return SafeArea(
          child: Stack(
        children: [
          Positioned(left: 0, right:0, top: height*0.08, child: Image.asset("assets/images/art-stairs@3x.png"), height: height*.45*space,),
          Positioned(left: width*0.1, top: height*.6, child: Text("Your Premium Cloud", style: titleTextStyle,)),
          Positioned(left: width*0.1, top: height*.65, child: Text("Launch your next\ncampaign within minutes\nwith Cloud Campaign\nMonitor.", style: subTitleTextStyle,)),
          
        ],
      ),
    );
  }
}