import 'dart:convert';
import 'package:flutter/services.dart' show rootBundle;
import 'dart:io';
import 'package:path_provider/path_provider.dart';

Future<void> process() async {
  try {
    // Load the file content as a string
    final fileContent = await rootBundle.loadString('assets/i18n/translations.json');

    // Split the content into lines
    final lines = LineSplitter.split(fileContent);

    // Iterate through each line and process it
    for (String line in lines) {
      if(line.startsWith("title"))
        {
          while(line != '}')
            {


            }

        }



      print(line);
    }
  } catch (e) {
    print('Error reading file: $e');
  }
}


Future<void> inputInfo(String target) async {
  try {
    // Get the documents directory
    final directory = await getApplicationDocumentsDirectory();

    // Define the file path (you can't use "assets", so use a writable directory)
    final filePath = '${directory.path}/i18n/translations.json';

    // Create a file and write some JSON content to it
    final file = File(filePath);
    const jsonContent = '''
    {
      "greeting": "Hello",
      "farewell": "Goodbye"
    }
    ''';
    await file.writeAsString(jsonContent);

    print('File created at: $filePath');
  } catch (e) {
    print('Error creating file: $e');
  }
}