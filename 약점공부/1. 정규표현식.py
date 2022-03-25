# https://programmers.co.kr/learn/courses/11

import re
# 1. 문자 클래스 [] : []안의 문자들과 매치
re.compile('[abc]')  # abc
# \d : 숫자
# \s : white space
# \w : 문자+숫자

# 2. Dot(.) : 줄바꿈을 제외한 모든 문자와 매치
re.compile('a.c')  # abc, adc, a8c ...
re.compile('a[.]b')  # a.b

# 3. * : 반복
re.compile('ab*')  # a, ab, abb, abbb ...

# 4. + : 반복
re.compile('ab+')  # ab, abb, abbb ...

# 5. {} : 반복
re.compile('ab{2}')  # abb
re.compile('ab{1,3}')  # ab, abb, abbb

# 6. ? : 있거나 없거나
re.compile('ab?c')  # ac, abc

# 7. | : OR
# 8. ^ : 앞에서 부터, []안에서는 not
# 9. $ : 뒤에서 부터

# re 모듈
# 0. re.compile() : 정규식 생성
p = re.compile('[a-z]+')
# 1. re.match() : 처음부터 정규식과 매치되는지 조사
m = p.match('python')
m = p.match('3 python')  # None

# 2. re.search() : 문자열 전첼를 탐색해서 매치되는지 조사
m = p.search('python')
m = p.search('3 python')

# 3. re.findall() : 매치되는 모든 문자열을 리스트로 반환
m = p.findall('life is too short')  # ['life', 'is', 'too', 'short']

# 4. re.sub() : 매치되는 문자열을 수정
m = p.sub('a_k_c', '*')  # *_*_*

# match 객체의 메서드 : 범위를 반환
# 1. group() : 합친 결과 값
# 2. start() : 시작 인덱스
# 3. end() : 마지막 인덱스
# 4. span() : 결과 값의 범위

# 그루핑 : ()
m = p.search('ABCABCABC OK?')
m.grout()  # 글룹의 일부만 값 가져오기 가능
