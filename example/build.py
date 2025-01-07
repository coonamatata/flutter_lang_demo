import yaml
import json

with open('assets/i18n/translations.yaml', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

def processAndOutput(target):
    store = {
        "app_bar": {
            "title": data['app_bar']['title'][target]
        },
        "button": {
            "cancel": data['button']['cancel'][target],
            "change_language": data['button']['change_language'][target]
        },
        "language": {
            "name": {
                "en_US": data['language']['name']['en_US'],
                "en_GB": data['language']['name']['en_GB'],
                "zh": data['language']['name']['zh'],
                "ja": data['language']['name']['ja'],
                "de": data['language']['name']['de'],
                "es": data['language']['name']['es'],
                "hi": data['language']['name']['hi'],
                "mi": data['language']['name']['mi'],
                "vi": data['language']['name']['vi']
            },
            "selected_message": data['language']['selected_message'][target],
            "selection": {
                "message": data['language']['selection']['message'][target],
                "title": data['language']['selection']['title'][target]
            }
        },
        "plural": {
            "demo": {
                "zero": data['plural']['demo']['zero'][target],
                "one": data['plural']['demo']['one'][target],
                "two": data['plural']['demo']['two'][target],
                "other": data['plural']['demo']['other'][target]
            }
        }
    }

    with open(f'assets/i18n/{target}.json', 'w', encoding='utf-8') as f0:
        json.dump(store, f0, ensure_ascii=False, indent=4)





#processing and outputting
processAndOutput("en_GB")
processAndOutput("en_US")
processAndOutput("vi")
processAndOutput("hi")
processAndOutput("es")
processAndOutput("de")
processAndOutput("mi")
processAndOutput("zh")
processAndOutput("ja")