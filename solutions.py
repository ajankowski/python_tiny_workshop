import yaml

file = open("solutions.yaml", 'r')
solutions_file = yaml.load(file)

def hint(exercise, solution=0):
    global solutions_file
    e = solutions_file[exercise]
    if solution:
        print(f"solution:\n-----\n{e['solution']}\n------")
    else:
        print(f"hint:\n------\n{e['hint']}\n------")
