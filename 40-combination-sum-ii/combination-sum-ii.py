class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        
        def backtrack(remain, start, path):
            if remain == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # If the current number exceeds the remaining target, stop further exploration
                if candidates[i] > remain:
                    break
                
                # Skip duplicates at the same tree level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(remain - candidates[i], i + 1, path)
                path.pop()
                
        backtrack(target, 0, [])
        return res