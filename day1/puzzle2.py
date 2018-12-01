import itertools, time

initialTime = time.time()

frequency = 0
frequencies = set()
lines = [line.strip('\n') for line in open("input/input.txt")]

for line in itertools.cycle(lines):
    frequency += int(line)
    if frequency in frequencies:
        break
    else:
        frequencies.add(frequency)

end = time.time() - initialTime

print("Result: %s" % frequency)
print("Time: %s" % end)