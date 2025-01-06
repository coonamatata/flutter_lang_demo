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
hid = {
    "app_bar": {
        "title": data['app_bar']['title']['hi']
    },
    "button": {
        "cancel": data['button']['cancel']['hi'],
        "change_language": data['button']['change_language']['hi']
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
        "selected_message": data['language']['selected_message']['hi'],
        "selection": {
            "message": data['language']['selection']['message']['hi'],
            "title": data['language']['selection']['title']['hi']
        }
    },
    "plural": {
        "demo": {
            "zero": data['plural']['demo']['zero']['hi'],
            "one": data['plural']['demo']['one']['hi'],
            "two": data['plural']['demo']['two']['hi'],
            "other": data['plural']['demo']['other']['hi']
        }
    }
}
with open('assets/i18n/hi.json', 'w', encoding='utf-8') as f3:
    json.dump(hid, f3, ensure_ascii=False, indent=4)
#zh
zhd = {
    "app_bar": {
        "title": data['app_bar']['title']['zh']
    },
    "button": {
        "cancel": data['button']['cancel']['zh'],
        "change_language": data['button']['change_language']['zh']
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
        "selected_message": data['language']['selected_message']['zh'],
        "selection": {
            "message": data['language']['selection']['message']['zh'],
            "title": data['language']['selection']['title']['zh']
        }
    },
    "plural": {
        "demo": {
            "zero": data['plural']['demo']['zero']['zh'],
            "one": data['plural']['demo']['one']['zh'],
            "two": data['plural']['demo']['two']['zh'],
            "other": data['plural']['demo']['other']['zh']
        }
    }
}

with open('assets/i18n/zh.json', 'w', encoding='utf-8') as f4:
    json.dump(zhd, f4, ensure_ascii=False, indent=4)
#ja
jad = {
    "app_bar": {
        "title": data['app_bar']['title']['ja']
    },
    "button": {
        "cancel": data['button']['cancel']['ja'],
        "change_language": data['button']['change_language']['ja']
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
        "selected_message": data['language']['selected_message']['ja'],
        "selection": {
            "message": data['language']['selection']['message']['ja'],
            "title": data['language']['selection']['title']['ja']
        }
    },
    "plural": {
        "demo": {
            "zero": data['plural']['demo']['zero']['ja'],
            "one": data['plural']['demo']['one']['ja'],
            "two": data['plural']['demo']['two']['ja'],
            "other": data['plural']['demo']['other']['ja']
        }
    }
}
with open('assets/i18n/ja.json', 'w', encoding='utf-8') as f5:
    json.dump(jad, f5, ensure_ascii=False, indent=4)
#de
ded = {
    "app_bar": {
        "title": data['app_bar']['title']['de']
    },
    "button": {
        "cancel": data['button']['cancel']['de'],
        "change_language": data['button']['change_language']['de']
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
        "selected_message": data['language']['selected_message']['de'],
        "selection": {
            "message": data['language']['selection']['message']['de'],
            "title": data['language']['selection']['title']['de']
        }
    },
    "plural": {
        "demo": {
            "zero": data['plural']['demo']['zero']['de'],
            "one": data['plural']['demo']['one']['de'],
            "two": data['plural']['demo']['two']['de'],
            "other": data['plural']['demo']['other']['de']
        }
    }
}
with open('assets/i18n/de.json', 'w', encoding='utf-8') as f6:
    json.dump(ded, f6, ensure_ascii=False, indent=4)
#es
esd = {
    "app_bar": {
        "title": data['app_bar']['title']['es']
    },
    "button": {
        "cancel": data['button']['cancel']['es'],
        "change_language": data['button']['change_language']['es']
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
        "selected_message": data['language']['selected_message']['es'],
        "selection": {
            "message": data['language']['selection']['message']['es'],
            "title": data['language']['selection']['title']['es']
        }
    },
    "plural": {
        "demo": {
            "zero": data['plural']['demo']['zero']['es'],
            "one": data['plural']['demo']['one']['es'],
            "two": data['plural']['demo']['two']['es'],
            "other": data['plural']['demo']['other']['es']
        }
    }
}
with open('assets/i18n/es.json', 'w', encoding='utf-8') as f7:
    json.dump(esd, f7, ensure_ascii=False, indent=4)
#mi
mid = {
    "app_bar": {
        "title": data['app_bar']['title']['mi']
    },
    "button": {
        "cancel": data['button']['cancel']['mi'],
        "change_language": data['button']['change_language']['mi']
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
        "selected_message": data['language']['selected_message']['mi'],
        "selection": {
            "message": data['language']['selection']['message']['mi'],
            "title": data['language']['selection']['title']['mi']
        }
    },
    "plural": {
        "demo": {
            "zero": data['plural']['demo']['zero']['mi'],
            "one": data['plural']['demo']['one']['mi'],
            "two": data['plural']['demo']['two']['mi'],
            "other": data['plural']['demo']['other']['mi']
        }
    }
}

with open('assets/i18n/mi.json', 'w', encoding='utf-8') as f8:
    json.dump(mid, f8, ensure_ascii=False, indent=4)
