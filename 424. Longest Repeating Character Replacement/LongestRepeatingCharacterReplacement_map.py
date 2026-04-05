class Solution(object):
    def is_valid_window(self, map, k):
        total_count = max_count = 0
        for i in range(26):
            char = chr(i + 65)
            if char in map:
                total_count += map[char]
                max_count = max(max_count, map[char])
        return total_count - max_count <= k

    def characterReplacement(self, s, k):
        i = j = 0
        map = {}
        map[s[i]] = 1
        max_window = 0

        while j < len(s):
            if self.is_valid_window(map, k):
                max_window = max(max_window, j - i + 1)
                j += 1
                if j < len(s):
                    map[s[j]] = map.get(s[j], 0) + 1
            else:
                map[s[i]] -= 1
                i += 1

        return max_window 