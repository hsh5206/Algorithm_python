# https://programmers.co.kr/learn/courses/30/lessons/12948
import re


def solution(phone_number):
    return re.sub(r'\d(?=\d{4})', '*', phone_number)
