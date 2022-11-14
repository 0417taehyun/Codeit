# 1. 데이터 사이언스란? | 06. 선수 과제: 개인적인 추가 내용

def is_onordered_palindrome(word: str) -> bool:
    table: dict[str, int] = {}
    for character in word:
        if character in table:
            table[character] += 1
        else:
            table[character] = 1
    
    odd_count: int = 0
    for count in table.values():
        if count % 2 == 1:
            odd_count += 1
    
    return True if odd_count <= 1 else False


def bit_manipulation(word: str) -> bool:
    answer: int = 0
    words: set = set(word)
    
    for character in word:
        answer ^= ord(character)
        
    if answer == 0 or chr(answer) in words:
        return True
    else:
        return False


if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | bool]] = [
        {
            "input": { "word": "abca" },
            "output": False
        },
        {
            "input": { "word": "babca" },
            "output": True
        },
        {
            "input": { "word": "bbaa" },
            "output": True
        },
        {
            "input": { "word": "dbdbacad" },
            "output": False
        }                  
    ]
    for case in cases:
        assert case["output"] == is_onordered_palindrome(**case["input"])
        assert case["output"] == bit_manipulation(**case["input"])
        