import yaml

with open('assets/i18n/translations.json', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

print(data['button']['cancel'])

#en_GB
en_GBd = {}
en_GBd['app_bar.title'] = data['app_bar']['title']['en_GB']
en_GBd['button.cancel'] = data['button']['cancel']['en_GB']
en_GBd['button.change_language'] = data['button']['change_language']['en_GB']
en_GBd['language.name'] = data['language']['name']['en_GB']
en_GBd['language.selected_message'] = data['language']['selected_message']['en_GB']
en_GBd['language.selection.title'] = data['language']['selection']['title']['en_GB']
en_GBd['language.selection.message'] = data['language']['selection']['message']['en_GB']
en_GBd['plural.demo.zero'] = data['plural']['demo']['zero']['en_GB']
en_GBd['plural.demo.one'] = data['plural']['demo']['one']['en_GB']
en_GBd['plural.demo.two'] = data['plural']['demo']['two']['en_GB']
en_GBd['plural.demo.other'] = data['plural']['demo']['other']['en_GB']


with open('assets/i18n/en_GB.json', 'w', encoding='utf-8') as f1:
    en_GBd = yaml.dump(en_GBd, f1, sort_keys=False)
#en_US

#vi

#hi

#zh

#ja

#de

#es

#mi



