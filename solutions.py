import yaml

file = open("solutions.yaml", 'rt', encoding='utf-8')
solutions_file = yaml.load(file)

def hint(exercise, solution=1):
    global solutions_file
    e = solutions_file[exercise]
    if solution:
        print(f"solution:\n-----\n{e['solution']}\n------")
    else:
        print(f"hint:\n------\n{e['hint']}\n------")
