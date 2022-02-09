def hanoi(n, source, helper, target):
    if n > 0:
        # move n-1 disks from the source to the target peg
        hanoi(n - 1, source, target, helper)
        # move the remaining disk from the source peg to the target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)


source = [4, 3, 2, 1]
target = []
helper = []
hanoi(len(source), source, helper, target)

print(source, helper, target)
