import codecs

with codecs.open('insurance.ipynb', 'r', 'utf-8') as f:
    c = f.read()

c = c.replace("x = final_df.drop('charges',axis = 1)", "X = final_df.drop('charges',axis = 1)")

with codecs.open('insurance.ipynb', 'w', 'utf-8') as f:
    f.write(c)
print("done")
