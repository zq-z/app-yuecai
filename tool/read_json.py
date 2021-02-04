import json


def read_json(filename):
    filepath = "../data/" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == '__main__':

    datas = read_json("login.json")
    airs = []
    for data in datas.values():
        airs.append((data.get("username"),
                     data.get("password"),
                     data.get("result_except"),
                     #data.get("success")
                     )
                    )
    print(airs)