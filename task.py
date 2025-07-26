import spacy

nlp = spacy.load("en_core_web_sm")

text = """
John Doe is a Data Scientist at Google working in the Bengaluru office.
He joined the company in August 2022 and specializes in NLP and Python.
"""

doc = nlp(text)

print("📌 Named Entities Found:\n")
for ent in doc.ents:
    print(f"{ent.text:<20} | {ent.label_}")
    
