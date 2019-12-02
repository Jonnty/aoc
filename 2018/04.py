# Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
# What is the ID of the guard you chose multiplied by the minute you chose?

import sys
import re
import operator
from collections import defaultdict

timestamp_pattern = R"\[\d{4}-\d\d-\d\d \d\d\:(\d\d)\]"

shift_start = re.compile(timestamp_pattern + R" Guard \#(\d+) begins shift")

sleep = re.compile(timestamp_pattern + " falls asleep")
wakes = re.compile(timestamp_pattern + " wakes up")

guard = None
asleep_at = None

guard_sleep_totals = defaultdict(int)

guard_minute_totals = defaultdict(lambda: defaultdict(int))

def guard_asleep(guard, start, stop):
    guard_sleep_totals[guard] += stop - start
    for minute in xrange(start, stop):
        guard_minute_totals[guard][minute] += 1

for line in sys.stdin.readlines():
    if shift_start.match(line):
        m = shift_start.match(line)
        if asleep_at is not None:
            guard_asleep(guard, asleep_at, 60)
        guard = int(m.group(2))
        asleep_at = None
        #print "shift start " + m.group(1) + " guard " + m.group(2)
    elif sleep.match(line):
        m = sleep.match(line)
        now = int(m.group(1))
        # if asleep_at:
        #     guard_asleep(guard, asleep_at, 60)
        #     guard_asleep(guard, 0, now)
        asleep_at = now
        #print "sleep " + m.group(1)
    elif wakes.match(line):
        m = wakes.match(line)
        now = int(m.group(1))
        # if asleep_at is None:
        #     asleep_at = 0
        guard_asleep(guard, asleep_at, now)
        asleep_at = None
        #print "wake " + m.group(1)
if asleep_at is not None:
    guard_asleep(guard, asleep_at, 60)

max_guard = mx = max(guard_sleep_totals.iteritems(), key=operator.itemgetter(1))[0]
for guard in guard_sleep_totals:
    print guard, guard_sleep_totals[guard]
print "---"
guard_to_max_minute = {}
max_minute = max(guard_minute_totals[max_guard].iteritems(), key=operator.itemgetter(1))[0]
for guard in guard_minute_totals:
    mx = max(guard_minute_totals[guard].iteritems(), key=operator.itemgetter(1))
    print guard, mx
print

print max_guard, max_minute
