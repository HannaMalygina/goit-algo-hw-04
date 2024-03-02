def total_salary(path):

    sum = 0
    ave = 0
    nof_empl = 0
    lines = []
    try:
        with open (path, "r", encoding = "utf-8") as fh:
            lines = [el for el in fh.readlines()]
    except FileNotFoundError:
        print (f"File {path} was not found")
    for line in lines:
        if line: 
            try:
                sum += float(line.split(",")[1])
            except IndexError:
                print("A line in the file has wrong format. Must be: 'name','salary'. I go to the next line")
                continue
            nof_empl += 1
    if nof_empl > 0: ave = sum / nof_empl
    
    return sum, ave

total, average = total_salary("sal.txt")
print (f"{total = } {average = }")