import yaml

with open('assets/i18n/translations.json', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

print(data['button']['cancel']['en_US'])
