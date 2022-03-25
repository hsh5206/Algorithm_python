class Trie():
    head = [0, dict()]

    def add(self, word):
        current = self.head
        current[0] += 1
        for x in word:
            if x not in current[1]:
                current[1][x] = [0, dict()]
            current = current[1][x]
            current[0] += 1

    def check(self, word):
        current = self.head
        result = 0
        for x in word:
            if current[0] == 1:
                return result
            result += 1
            current = current[1][x]
        return result


def solution(words):
    answer = 0
    T = Trie()
    for word in words:
        T.add(word)
    for word in words:
        answer += T.check(word)
    return answer
