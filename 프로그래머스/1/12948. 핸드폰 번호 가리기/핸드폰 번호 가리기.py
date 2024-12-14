def solution(phone_number):
    star_count = len(phone_number) - 4
    last_four = phone_number[-4:]
    
    return "*" * star_count + last_four