marks = [75, 32, 88, 40, 27, 59, 90, 38, 45, 60]
result={
    "Pass": [],
    "Fail": []
}
for mark in marks:
    if mark >=40:
        result["Pass"].append(mark)
    else:
        result["Fail"].append(mark)
print("Pass:", result["Pass"])
print("Fail:", result["Fail"])