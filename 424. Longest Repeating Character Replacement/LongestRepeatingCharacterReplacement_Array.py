class Solution(object):
    def is_valid_window(self, count, k):
        total_count = sum(count)
        max_count = max(count)
        return total_count - max_count <= k

    def characterReplacement(self, s, k):
        i = j = 0
        count = [0] * 26
        count[ord(s[0]) - ord('A')] = 1
        max_window = 0

        while j < len(s):
            if self.is_valid_window(count, k):
                max_window = max(max_window, j - i + 1)
                j += 1
                if j < len(s):
                    count[ord(s[j]) - ord('A')] += 1
            else:
                count[ord(s[i]) - ord('A')] -= 1
                i += 1
        return max_window