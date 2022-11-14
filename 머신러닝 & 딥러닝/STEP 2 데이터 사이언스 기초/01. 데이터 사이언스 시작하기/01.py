# 1. 데이터 사이언스란? | 06. 선수 과제

def is_palindrome(word: str) -> bool:
    start, end = 0, len(word)-1
    while start < end:
        if word[start] != word[end]:
            return False
        
        start, end = start+1, end-1
        
    return True
    

if __name__ == "__main__":
    cases: list[dict[str, dict[str, str] | bool]] = [
        {
            "input": {"word": "racecar"},
            "output": True
        },
        {
            "input": {"word": "stars"},
            "output": False
        },
        {
            "input": {"word": "토마토"},
            "output": True
        },
        {
            "input": {"word": "kayak"},
            "output": True
        },
        {
            "input": {"word": "hello"},
            "output": False
        }                                
    ]
    for case in cases:
        assert case["output"] == is_palindrome(**case["input"])
        