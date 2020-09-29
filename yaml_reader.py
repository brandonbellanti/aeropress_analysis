import yaml

test_filepath = 'brew_record.yml'

with open(test_filepath,'r') as yaml_file:
    data = yaml.load(yaml_file)
    print(type(data))