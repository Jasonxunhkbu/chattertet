import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import ToneAnalyzerV3
tone_analyzer = ToneAnalyzerV3(
  username='ae308016-2e9e-4e15-949f-cffeddf20842',
  password='xqIobDGObduw',
  version='2016-05-19'
)

with open(join(dirname(__file__),'test_tone.json')) as tone_json:
  tone = tone_analyzer.tone_chat(json.load(tone_json)['utterances'])

print(json.dumps(tone, indent=2))
