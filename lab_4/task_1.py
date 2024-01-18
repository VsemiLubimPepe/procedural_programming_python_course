import json

# TODO решите задачу
def task() -> float:
    with open("input.json", "r") as in_file:
        file_data = json.load(in_file)
    result = sum([row["score"] * row["weight"] for row in file_data])
    return round(result, 3)


print(task())
