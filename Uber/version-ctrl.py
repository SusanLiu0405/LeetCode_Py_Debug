def find_largest_branch(logs):
    branches = {}
    current_branch = None

    for log in logs:
        parts = log.split()
        command, argument = parts[0], parts[1]

        if command == "switch":
            current_branch = argument
            if current_branch not in branches:
                branches[current_branch] = set()

        elif command == "push":
            if current_branch:
                branches[current_branch].add(argument)

    largest_branch = max(branches, key=lambda branch: len(branches[branch]))
    return largest_branch


logs = [
    "switch branch1",
    "push file1",
    "push file2",
    "push file1",
    "switch branch2",
    "switch issue2",
    "push file1",
    "push file2",
    "push file3"
]
print(find_largest_branch(logs))
