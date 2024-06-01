print([x for x in range(78, 90)])
with open(".venv/Lib/site-packages/multiselectfield/db/fields.py", "w") as f:
    d = f.readlines()
    f.seek(0)
    if 'def _get_flatchoices(self):' in d[77]:
        for i in range(len(d)):
            if i not in [x for x in range(77, 90)]:
                f.write(d[i])
    f.truncate()
    f.close()