import 'package:flutter/material.dart';

class AccountButtonWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: double.infinity,
      child: Row(
        children: [
          Expanded(
            child: SizedBox(),
            flex: 1,
          ),
          Expanded(
            child: RaisedButton(
              padding: const EdgeInsets.all(24),
              color: Color(0xFF7442F0),
              textTheme: Theme.of(context).buttonTheme.textTheme,
              shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(10)),
              onPressed: () {},
              child: Text("Create an account", style: TextStyle(color: Colors.white, fontSize: 22),),
            ),
            flex: 20,
          ),
          Expanded(
            child: SizedBox(),
            flex: 1,
          )
        ],
      ),
    );
  }
}
