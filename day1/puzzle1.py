import time

initialTime = time.time()

frequency = 0
lines = [line.strip('\n') for line in open("input/input.txt")]

for line in lines:
    frequency += int(line)

end = time.time() - initialTime

print("result: %s" % frequency)
print("time: %s" % end)