

import 'package:flutter/material.dart';

class IntroView0 extends StatelessWidget {
  
  final double space;
  
  IntroView0(this.space);

  @override
  Widget build(BuildContext context) {
    final width =  MediaQuery.of(context).size.width;
    final height = MediaQuery.of(context).size.height;
    final titleTextStyle = TextStyle(fontSize: 20, fontWeight: FontWeight.w800, color: Color(0xCC7442F0));
    final subTitleTextStyle = TextStyle(fontSize: 32, fontWeight: FontWeight.w800, color: Colors.black);
    final nextTextStyle = TextStyle(fontSize: 16, fontWeight: FontWeight.w600, color: Color(0xCC7442F0));
    return SafeArea(
          child: Stack(
        children: [
          Positioned(left: 150 - ((1-space)* 150), top: height*0.08, child: Image.asset("assets/images/art-cloud@3x.png", width: width * 0.5)),
          Positioned(right: 400*space, top: height*0.3, child: Image.asset("assets/images/art-work@3x.png", width:  width * 0.5 * (1-space))),
          Positioned(left: width*0.1, top: height*.54, child: Text("Hello!", style: titleTextStyle,)),
          Positioned(left: width*0.1, top: height*.59, child: Text("Your own \nprivate Cloud is\none step away.", style: subTitleTextStyle,)),
          Positioned(left: width*0.1, top: height*.8, child: Text("Swipe left to get started", style: nextTextStyle,))
        ],
      ),
    );
  }
}