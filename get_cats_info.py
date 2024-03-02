def get_cats_info(path):
    cats = list()
    lines = []
    try:
        with open (path, "r", encoding = "utf-8") as fh:
            lines = [el for el in fh.readlines()]
    except FileNotFoundError:
        print (f"File {path} was not found")

    for line in lines:
        splited_line = line.split(",")
        try:
            cats.append({"id": splited_line[0], "name": splited_line[1], "age": splited_line[2].strip()})
        except IndexError:
            print("A line in the file has wrong format. Must be: 'id','name','age'. I go to the next line")
            continue

    return cats

print(get_cats_info("cats1.txt"))