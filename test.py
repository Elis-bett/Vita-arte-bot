import json
with open('testing.json', encoding='utf-8') as test_file:
    data = json.load(test_file)
tests = data['tests']