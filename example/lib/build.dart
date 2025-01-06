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
    bool appBarDone = false;

    // Iterate through each line and process it
    for (String line in lines) {
      if(line.startsWith("title"))
        {
          if(appBarDone){
            while(line != '}') {
              if(line.substring(0,7).contains("en_")) {
                inputInfo(line.substring(1,5));
              } else {
                inputInfo(line.substring(1,3));
              }
            }
          } else {
            while(line != '}')
            {
              if(line.substring(0,7).contains("en_")) {
                inputInfo(line.substring(1,5));
              } else {
                inputInfo(line.substring(1,3));
              }
            }
            appBarDone = true;
          }
        }
      if(line.startsWith("cancel"))
      {
        while(line != '}')
        {
          if(line.substring(0,7).contains("en_")) {
            inputInfo(line.substring(1,5));
          } else {
            inputInfo(line.substring(1,3));
          }
        }
      }
      if(line.startsWith("change_language"))
      {
        while(line != '}')
        {
          if(line.substring(0,7).contains("en_")) {
            inputInfo(line.substring(1,5));
          } else {
            inputInfo(line.substring(1,3));
          }
        }
      }
      if(line.startsWith("name"))
      {
        while(line != '}')
        {
          if(line.substring(0,7).contains("en_")) {
            inputInfo(line.substring(1,5));
          } else {
            inputInfo(line.substring(1,3));
          }
        }
      }
      if(line.startsWith("selected_message"))
      {
        while(line != '}')
        {
          if(line.substring(0,7).contains("en_")) {
            inputInfo(line.substring(1,5));
          } else {
            inputInfo(line.substring(1,3));
          }
        }
      }
      if(line.startsWith("zero"))
      {
        while(line != '}')
        {
          if(line.substring(0,7).contains("en_")) {
            inputInfo(line.substring(1,5));
          } else {
            inputInfo(line.substring(1,3));
          }
        }
      }
      if(line.startsWith("message"))
      {
        while(line != '}')
        {
          if(line.substring(0,7).contains("en_")) {
            inputInfo(line.substring(1,5));
          } else {
            inputInfo(line.substring(1,3));
          }
        }
      }
      if(line.startsWith("one"))
      {
        while(line != '}')
        {
          if(line.substring(0,7).contains("en_")) {
            inputInfo(line.substring(1,5));
          } else {
            inputInfo(line.substring(1,3));
          }
        }
      }
      if(line.startsWith("two"))
      {
        while(line != '}')
        {
          if(line.substring(0,7).contains("en_")) {
            inputInfo(line.substring(1,5));
          } else {
            inputInfo(line.substring(1,3));
          }
        }
      }
      if(line.startsWith("other"))
      {
        while(line != '}')
        {
          if(line.substring(0,7).contains("en_")) {
            inputInfo(line.substring(1,5));
          } else {
            inputInfo(line.substring(1,3));
          }
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