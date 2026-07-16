def hanoi_solver(n):
    # Create the three rods
    rods = [list(range(n, 0, -1)), [], []]

    # Store every step
    steps = []

    def record():
        steps.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move(disks, source, auxiliary, target):
        if disks == 1:
            rods[target].append(rods[source].pop())
            record()
        else:
            move(disks - 1, source, target, auxiliary)
            rods[target].append(rods[source].pop())
            record()
            move(disks - 1, auxiliary, source, target)

    # Record initial state
    record()

    # Solve Hanoi
    move(n, 0, 1, 2)

    # Return as a single string
    return "\n".join(steps)


# Testing
print(hanoi_solver(2))
