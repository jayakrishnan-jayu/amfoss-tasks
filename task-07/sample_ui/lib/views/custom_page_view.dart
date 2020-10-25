import 'package:flutter/material.dart';
import 'package:sample_ui/views/intro_view_1.dart';
import 'package:sample_ui/views/intro_view_0.dart';
import 'package:dots_indicator/dots_indicator.dart';

class CustomPageView extends StatefulWidget {
  @override
   CustomPageViewState createState() =>  CustomPageViewState();
}

class  CustomPageViewState extends State <CustomPageView>{

  PageController _pageController;
  double _currentPage = 0.0;
  double space = 0.5;
  bool animate = false;

  @override
  void initState() {
    _pageController = PageController();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
        children: [
          NotificationListener<ScrollNotification>(
            onNotification: (notification) {
              final metrics = notification.metrics;
              if (metrics is PageMetrics) {
                setState(
                  () {
                    _currentPage = metrics.page;
                    
                      setState(() {
                        space = _currentPage;
                      });
                  },
                );
              }
              return false;
            },
            child: PageView(
              controller: _pageController,
              physics: const BouncingScrollPhysics(),
              children: [IntroView0(space), IntroView1(space)],
            ),
          ),
          Positioned(
            left: 1,
            right: 1,
            top: 16,
            child: SafeArea(
                child: DotsIndicator(
              dotsCount: 2,
              position: _currentPage,
              decorator: DotsDecorator(
                size: const Size.square(9.0),
                activeSize: const Size(88.0, 9.0),
                color: Color(0x557442F0),
                activeColor: Color(0xFF7442F0),
                activeShape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(5.0)),
              ),
            )),
          )
        ],
      );
  }
}
