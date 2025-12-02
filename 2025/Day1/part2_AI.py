pos, count = 50, 0

with open("2025/Day1/directions.txt") as f:
    for line in f:
        d, n = line[0], int(line[1:])
        new_pos = (pos + n if d == "R" else pos - n) % 100
        count += n // 100 + (
            new_pos == 0
            or (
                new_pos < pos
                if d == "R"
                else new_pos > pos and pos != 0 and new_pos != 0
            )
        )
        pos = new_pos

print(count)

"""
LOGIC FLOW EXPLANATION:
======================

Problem: Count how many times a dial pointer crosses or lands on position 0 during rotations.
- Dial has positions 0-99 (wraps around)
- Rotations: R (right/clockwise), L (left/counterclockwise)

Solution breakdown:
1. pos, count = 50, 0
   - Start at position 50, initialize counter

2. For each rotation instruction:
   - Parse: d = direction ('R' or 'L'), n = rotation amount
   
3. Calculate new position:
   - R: (pos + n) % 100  (move clockwise)
   - L: (pos - n) % 100  (move counterclockwise, Python handles negative modulo correctly)

4. Count crossings/landings (complex expression broken down):
   count += n // 100 + (...)
   
   Part A: n // 100
   - Counts complete 100-unit cycles (each cycle = 1 crossing of position 0)
   
   Part B: (new_pos == 0 or ...)
   - Returns True (1) or False (0), added to count
   
   Case 1: new_pos == 0
   - We landed exactly on 0 → count it
   
   Case 2: For RIGHT rotations (new_pos < pos)
   - If new < pos, we wrapped around (crossed 0)
   - But only count if we didn't land on 0 (handled by Case 1)
   
   Case 3: For LEFT rotations (new_pos > pos and pos != 0 and new_pos != 0)
   - If new > pos, we wrapped around backwards (crossed 0)
   - Special: Don't count if we started at 0 (pos != 0)
   - Don't count if we landed on 0 (new_pos != 0, handled by Case 1)

5. Update position for next iteration

Example trace (from sample):
L68: pos=50 → new=82 (50-68=-18 → 82), crosses 0 once → count=1
L30: pos=82 → new=52, no wrap → count=1
R48: pos=52 → new=0, lands on 0 → count=2
L5:  pos=0 → new=95, no count (started at 0) → count=2
R60: pos=95 → new=55, wraps → count=3
L55: pos=55 → new=0, lands on 0 → count=4
L1:  pos=0 → new=99, no count (started at 0) → count=4
L99: pos=99 → new=0, lands on 0 → count=5
R14: pos=0 → new=14, no wrap → count=5
L82: pos=14 → new=32 (14-82=-68 → 32), wraps → count=6

Result: 6 times the dial pointed at 0
"""
