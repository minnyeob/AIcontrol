# abcdefghijklmnop
# 123456789
# 가나다라마사아자차카타파하

# https://iamfreeman.tistory.com/entry/vi-vim-%ED%8E%B8%EC%A7%91%EA%B8%B0-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%A0%95%EB%A6%AC-%EB%8B%A8%EC%B6%95%ED%82%A4-%EB%AA%A8%EC%9D%8C-%EB%AA%A9%EB%A1%9D
# ㄴ참고 링크

a_val = [0,1,2]
    
print ("hello World")

for i in a_val:
    print("hello", i)
    
#vim 단축키
# 시행 전 키보드가 "한글"모드 확인, capslock 확인
# 아래의 +는 "+"를 입력하는 것이 아니라 동시에 입력하라는 표시임

# 문자 삽입

# a                 커서기뒤 글쓰기
# i                 커서 앞 글쓰기

# A                 글자 맨 뒤 글쓰기
# I                 글자 맨 앞 글동기

# o                 현재 위치 아래에 한줄만들기
# O                 현재 위치 위에 한줄 만들기

# [esc]             입력 종료

# ////////////////////////////////////////////////////////

# 커서 이동법

# h                 커서를 좌로 이동
# l                 커서를 우로 이동
# j                 커서를 아래로 이동
# k                 커서를 위로 이동

# H                 문서의 위로 이동
# M                 문서의 중간으로 이동
# L                 문서의 아래로 이동

# e                 다음 단어 맨 뒤로 이동
# w                 다음 단어 맨 앞으로 이동

# [enter]           한줄 내려가기
# [back sapce]      커서 왼쪽으로 옮기기
# [space]           커서 오른쪽으로 옮기기

# ^                 줄 맨 앞으로 가기
# $                 줄 맨 뒤로 가기

# '숫자' + G(대문자) 원하는 '숫자' 번째 줄로 이동

# [ctrl] + i        화면의 아래로 이동
# [ctrl] + b        화면의 위로 이동

# [ctrl] + d        전체의 중간만큼 밑으로 이동
# [ctrl] + u        전체의 중간만큼 위으로 이동

# [ctrl] + e        한칸씩 밑으로 스크롤
# [ctrl] + y        한칸씩 위로 스크롤 

# //////////////////////////////////////////////////////////////

# 텍스트 변경

# c + w             단어변경
# c + c             행 변경
# C(대문자)         커서의 오른쪽의 행 변경
# s(소문자)         현재 위치의 문자열 대체
# S(대문자)         현재 위치의 라인의 문자열 대체
# r                 커서 위치 문자를 다른문자로 교체
# r + [enter]       행 분리
# J                 현재 줄과 아래 줄 결함
# x + p             커서 위치의 문자와 오른쪽 문자교환
# ~                 대문자 <-> 소문자
# u(소문자)         되돌리기
# U(대문자)         행 변경 사항 취소, 이전의 최종 행 취소
# .                 마지막 명령 반복

# x                 지우기
# (숫자) + x        (숫자)개 만큼 문자 지우기
# d + d             현재 라인 삭제
# (숫자) + d + d    현재 부터 (숫자)개수 만큼의 라인 지우기
# d + b             현재 위치의 거꾸로 단어 삭제
# D                 오른쪽 행 삭제
# :(숫자1),(숫자2)d  숫자1~숫자2번째 행 삭제

# y + y             현재 줄 복사
# Y(대문자)         행 복사
# y + h             커서의 왼쪽 문자 복사 
# y + 1             커서가 위치한 문자 복사
# y + i             커서가 위치한 줄 + 아랫줄 복사
# y + k             커서가 위치한 줄 + 윗줄 복사
# P(대문자)         현재 줄 위로 붙여넣기
# p(소문자)         현재 줄 아래로 붙여넣기

# :(숫자1),(숫자2) co (숫자3)       (숫자1) ~ (숫자2)행을 (숫자3)번째 행 뒤에 복사
# :(숫자1),(숫자2) co (숫자3)       (숫자1) ~ (숫자2)행을 (숫자3)번째 행 뒤로 이동

# /////////////////////////////////////////////////////////////////

# 행 설정

# :set nu or :set number    각 행 좌측에 번호 표시
# :set nonu                 각 행 좌측에 번호 숨기기

# G                         마지막 줄로 이동
# (숫자) + G                (숫자)번째 줄로 이동
# [ctrl] + G                현재 파일명과 라인 정보 표시


# ////////////////////////////////////////////////////////////////////

# 탐색

# / + (찾을 string)         위에서 아래 방향으로 문자열 검색
# ? + (찾을 string)         아래에서 위 방향으로 문자열 검색
# n                         문자열 계속 검색
# N                         문자열 이전 검색
# :g/search-string/s/       문자열 찾고 바꾸기
# 1,.s/string/rep           현재 행의 문자열을 rep형태로 바꾸기
# %s/string/rep/g           파일 전채를 rep형태로 바꾸침
# $/(string1)/(string2)     현재 커서로 부터 모든 (string1)을 (string2)로 교체

# //////////////////////////////////////////////////////////////////////////

# 화면 정리

# [ctrl] + 1                불필요한 화면 정리 후 새로고침 

# //////////////////////////////////////////////////////////////////////////

# 파일

# :r(파일명)                 현재 커서 다음에 파일 삽입
# :(행번호)r(파일명)          행번호 뒤에 다음 파일 삽입

# //////////////////////////////////////////////////////////////////////////////

# 저장 및 종료

# :w                        변경사항 저장
# :w(파일명)                (파일명)으로 변경사항 저장
# :w + q  or  ZZ            변경사항 저장후 vim 종료
# :q!                       변경사항 저장 안함 후 종료
# q                         수정사항 저장 안함 후 vim종료
# e!                        수정사항 저장 안함 후 편집모드


# //////////////////////////////////////////////////////////////////////////////

# 범위 지정

# .                 현재 줄
# %                 전체 줄
# $                 파일 맨 끝 줄
# (숫자),$          %같음
# (숫자1),(숫자2)    (숫자1)~(숫자2)번째 줄