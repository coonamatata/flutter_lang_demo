import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_translate/flutter_translate.dart';

void main() async {
  var delegate = await LocalizationDelegate.create(
    fallbackLocale: 'en_US',
    supportedLocales: [
      'en_US', // American English
      'en_GB', // British English
      'zh', // Simplified Chinese
      'ja', // Japanese
      'de', // German
      'es', // Spanish
      'hi', // Hindi
      'mi', // Māori
      'vi', // Vietnamese
    ],
  );

  runApp(LocalizedApp(delegate, MyApp()));
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var localizationDelegate = LocalizedApp.of(context).delegate;

    return LocalizationProvider(
      state: LocalizationProvider.of(context).state,
      child: MaterialApp(
        title: 'Flutter Translate Demo',
        localizationsDelegates: [
          GlobalMaterialLocalizations.delegate,
          GlobalWidgetsLocalizations.delegate,
          localizationDelegate
        ],
        supportedLocales: localizationDelegate.supportedLocales,
        locale: localizationDelegate.currentLocale,
        theme: ThemeData(primarySwatch: Colors.blue),
        home: MyHomePage(),
      ),
    );

  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, this.title}) : super(key: key);
  final String? title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _decrementCounter() => setState(() => _counter--);

  void _incrementCounter() => setState(() => _counter++);

  @override
  Widget build(BuildContext context) {
    var localizationDelegate = LocalizedApp.of(context).delegate;

    return Scaffold(
      appBar: AppBar(
        title: Text(translate('app_bar.title')),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(translate('language.selected_message', args: {'language': translate('language.name.${localizationDelegate.currentLocale.languageCode}')})),
            Padding(
              padding: EdgeInsets.only(top: 25, bottom: 160),
              child: CupertinoButton.filled(
                child: Text(translate('button.change_language')),
                padding: const EdgeInsets.symmetric(vertical: 10.0, horizontal: 36.0),
                onPressed: () => _onActionSheetPress(context),
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: Text(translatePlural('plural.demo', _counter)),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                IconButton(
                  icon: Icon(Icons.remove_circle),
                  iconSize: 48,
                  onPressed: _counter > 0 ? () => setState(() => _decrementCounter()) : null,
                ),
                IconButton(
                  icon: Icon(Icons.add_circle),
                  color: Colors.blue,
                  iconSize: 48,
                  onPressed: () => setState(() => _incrementCounter()),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  void showDemoActionSheet({required BuildContext context, required Widget child}) {
    showCupertinoModalPopup<String>(
      context: context,
      builder: (BuildContext context) => child,
    ).then((String? value) {
      if (value != null) {
        changeLocale(context, value);
      }
    });
  }

  void _onActionSheetPress(BuildContext context) {
    showDemoActionSheet(
      context: context,
      child: CupertinoActionSheet(
        title: Text(translate('language.selection.title')),
        message: Text(translate('language.selection.message')),
        actions: <Widget>[
          CupertinoActionSheetAction(
            child: Text(translate('language.name.en_US')), // American English
            onPressed: () => Navigator.pop(context, 'en_US'),
          ),
          CupertinoActionSheetAction(
            child: Text(translate('language.name.en_GB')), // British/Australia/NZ English
            onPressed: () => Navigator.pop(context, 'en_GB'),
          ),
          CupertinoActionSheetAction(
            child: Text(translate('language.name.zh')), // Simplified Chinese
            onPressed: () => Navigator.pop(context, 'zh'),
          ),
          CupertinoActionSheetAction(
            child: Text(translate('language.name.ja')), // Japanese
            onPressed: () => Navigator.pop(context, 'ja'),
          ),
          CupertinoActionSheetAction(
            child: Text(translate('language.name.de')), // German
            onPressed: () => Navigator.pop(context, 'de'),
          ),
          CupertinoActionSheetAction(
            child: Text(translate('language.name.es')), // Spanish
            onPressed: () => Navigator.pop(context, 'es'),
          ),
          CupertinoActionSheetAction(
            child: Text(translate('language.name.hi')), // Hindi
            onPressed: () => Navigator.pop(context, 'hi'),
          ),
          CupertinoActionSheetAction(
            child: Text(translate('language.name.mi')), // Māori
            onPressed: () => Navigator.pop(context, 'mi'),
          ),
          CupertinoActionSheetAction(
            child: Text(translate('language.name.vi')), // Vietnamese
            onPressed: () => Navigator.pop(context, 'vi'),
          ),
          CupertinoActionSheetAction(
            child: Text(translate('language.name.translations')), // American English
            onPressed: () => Navigator.pop(context, 'all'),
          ),
        ],
        cancelButton: CupertinoActionSheetAction(
          child: Text(translate('button.cancel')),
          isDefaultAction: true,
          onPressed: () => Navigator.pop(context, null),
        ),
      ),
    );
  }
}