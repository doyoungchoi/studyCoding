##️⃣ 프로그래머스: (해시) 전화번호 목록
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) <= len(phone_book[i+1]):
	        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
    	        return False
    return answer