import 'package:flutter/material.dart';
import 'package:sample_ui/views/custom_page_view.dart';
import 'package:sample_ui/widgets/account_button_widget.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Ubiquitous UI',
      theme: ThemeData(
          primarySwatch: Colors.blue,
          visualDensity: VisualDensity.adaptivePlatformDensity,
          textTheme: TextTheme(
              button: TextStyle(fontSize: 18.0, color: Colors.white))),
      home: Scaffold(
        body: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Expanded(
              child: Container(
                child: CustomPageView(),
              ),
              flex: 25,
            ),
            Expanded(
              child: Container(
                child: AccountButtonWidget(),
              ),
              flex: 3,
            )
          ],
        ),
      ),
    );
  }
}
