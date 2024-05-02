class Solution:
    def calPoints(self, operations: List[str]) -> int:
        end_scores = []
        for i, x in enumerate(operations):
            if x == '+':
                end_scores.append(end_scores[-1] + end_scores[-2])
            elif x == 'D':
                end_scores.append(end_scores[-1] * 2)
            elif x == 'C':
                end_scores.pop()
            else:
                end_scores.append(int(x))
        return sum(end_scores)
