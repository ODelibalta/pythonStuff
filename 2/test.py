text = "X-DSPAM-Confidence:    0.8475";
space = text.rfind(' ')
endpoint = len(text)
print text[space:endpoint]
