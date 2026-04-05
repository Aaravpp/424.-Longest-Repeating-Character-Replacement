We need to find the longest substring where we can replace at most k characters to make all characters identical.

Key observation:
In any window, if we know the frequency of the most common character (maxFreq), then:

replacements needed = window size − maxFreq

If replacements ≤ k → valid window ✅
Else → shrink window ❌

Approach
Use sliding window (two pointers):
i → left pointer
j → right pointer
Maintain a frequency array of size 26
Track:
maxFreq → highest frequency in current window
Expand window (j++)
If invalid:
Shrink window (i++)
Update maximum window length
Optimization:

Avoid recalculating frequencies every time (your current code does this → slower)

Complexity
Time complexity: O(n)
Space complexity: O(1)
(fixed size 26 array)
