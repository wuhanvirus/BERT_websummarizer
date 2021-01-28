import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from summarizer import Summarizer
import sys
import base64

text = sys.argv[1]
model = Summarizer()

result = model(text)
# result = model(text, min_length=20)
# result = model(text, min_length=20, max_length=80)
summary = "".join(result)


print(base64.b64encode(summary.encode('utf-8')))