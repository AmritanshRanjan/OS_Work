# availInst: The available instances of each resource type.
# needRes: The maximum resources that each process may need.
# currRes: The resources currently allocated to each process.

def safeState(processes, availInst, needRes, currRes):
    num_processes = len(processes)
    num_resources = len(availInst)
    # Calculate the need matrix
    need = []
    for i in range(num_processes):
        need_row = []
        for j in range(num_resources):
            need_row.append(needRes[i][j] - currRes[i][j])
        need.append(need_row)

    # Initialize work and finish
    work = availInst[:]
    finish = [False] * num_processes

    safe_sequence = []

    while len(safe_sequence) < num_processes:
        made_progress = False
        for i in range(num_processes):
            if not finish[i]:
                # Check if all needs can be satisfied with available resources
                if all(need[i][j] <= work[j] for j in range(num_resources)):
                    # Simulate the current resources
                    for j in range(num_resources):
                        work[j] += currRes[i][j]
                    finish[i] = True
                    safe_sequence.append(processes[i])
                    made_progress = True
        if not made_progress:
            return False, []

    return True, safe_sequence


# Example for how to use it
processes = [0, 1, 2, 3, 4]
availInst = [3, 3, 2]
needRes = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
currRes = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

is_safe_state, safe_sequence = safeState(processes,availInst, needRes, currRes)

#if else statement for a safe state
if safeState:
    print("The system is in a safe state.")
    print("Safe sequence:", safe_sequence)
else:
    print("The system is in an unsafe state. Deadlock may occur.")
