text = "X-DSPAM-Confidence:    0.8475";
start = text.find(':')
id = text[start+1:]
id = id.strip()
id = float(id)
print(id)
