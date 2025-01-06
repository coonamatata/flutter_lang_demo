import yaml
import json
with open('assets/i18n/translations.json', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

print(data['button']['cancel'])

#en_GB
en_GBd = {
    "app_bar": {
        "title": data['app_bar']['title']['en_GB']
    },
    "button": {
        "cancel": data['button']['cancel']['en_GB'],
        "change_language": data['button']['change_language']['en_GB']
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
        "selected_message": data['language']['selected_message']['en_GB'],
        "selection": {
            "message": data['language']['selection']['message']['en_GB'],
            "title": data['language']['selection']['title']['en_GB']
        }
    },
    "plural": {
        "demo": {
            "zero": data['plural']['demo']['zero']['en_GB'],
            "one": data['plural']['demo']['one']['en_GB'],
            "two": data['plural']['demo']['two']['en_GB'],
            "other": data['plural']['demo']['other']['en_GB']
        }
    }
}
with open('assets/i18n/en_GB.json', 'w', encoding='utf-8') as f1:
    json.dump(en_GBd, f1, ensure_ascii=False, indent=4)

#en_US
en_USd = {
    "app_bar": {
        "title": data['app_bar']['title']['en_US']
    },
    "button": {
        "cancel": data['button']['cancel']['en_US'],
        "change_language": data['button']['change_language']['en_US']
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
        "selected_message": data['language']['selected_message']['en_US'],
        "selection": {
            "message": data['language']['selection']['message']['en_US'],
            "title": data['language']['selection']['title']['en_US']
        }
    },
    "plural": {
        "demo": {
            "zero": data['plural']['demo']['zero']['en_US'],
            "one": data['plural']['demo']['one']['en_US'],
            "two": data['plural']['demo']['two']['en_US'],
            "other": data['plural']['demo']['other']['en_US']
        }
    }
}
with open('assets/i18n/en_US.json', 'w', encoding='utf-8') as f1:
    json.dump(en_USd, f1, ensure_ascii=False, indent=4)
#vi
vid = {
    "app_bar": {
        "title": data['app_bar']['title']['vi']
    },
    "button": {
        "cancel": data['button']['cancel']['vi'],
        "change_language": data['button']['change_language']['vi']
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
        "selected_message": data['language']['selected_message']['vi'],
        "selection": {
            "message": data['language']['selection']['message']['vi'],
            "title": data['language']['selection']['title']['vi']
        }
    },
    "plural": {
        "demo": {
            "zero": data['plural']['demo']['zero']['vi'],
            "one": data['plural']['demo']['one']['vi'],
            "two": data['plural']['demo']['two']['vi'],
            "other": data['plural']['demo']['other']['vi']
        }
    }
}
with open('assets/i18n/vi.json', 'w', encoding='utf-8') as f2:
    json.dump(vid, f2, ensure_ascii=False, indent=4)
#hi

#zh

#ja

#de

#es

#mi



