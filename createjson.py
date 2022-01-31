import sys
import json
import sqlite3
conn = sqlite3.connect('../../databases/cvm.db')


def exists(dicti, paperInfo):
    if "children" not in dicti.keys():
        if len(paperInfo) < 3:
            return [{"name": paperInfo[-2], "size": paperInfo[-1]}]
        else:

            return [{"name": paperInfo[0], "children": exists({}, paperInfo[1:])}]

    elif len(paperInfo) < 3:
        dicti["children"].append({"name": paperInfo[-2], "size": paperInfo[-1]})

    elif paperInfo[0] in [i["name"] for i in dicti["children"]]:
        for paper in dicti["children"]:
            if paperInfo[0] == paper["name"]:
                return exists(paper, paperInfo[1:])
    else:
        dicti["children"].append({"name": paperInfo[0], "children": exists({}, paperInfo[1:])})


def executeFuncs(cnpj):
    c = conn.cursor()
    c.execute("Select * from table_agregate where CNPJ_FUNDO ='" + cnpj + "'")
    portfolio = c.fetchall()
    js = {'name': 'FI', "children": []}
    for p in portfolio:
        exists(js, p)
    print(json.dumps(js))
    # with open("./current.json", "w") as outfile:
    #     json.dump(js, outfile)



executeFuncs(sys.argv[1])
