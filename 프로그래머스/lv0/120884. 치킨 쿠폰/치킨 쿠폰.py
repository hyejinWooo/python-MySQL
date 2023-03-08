# def solution(chicken):
#     answer = 0
#     while answer // 10 == 0:
#         answer = answer + chicken // 10
#     return answer
# 108 마리를 쿠폰으로 시킬 수 있고 쿠폰 1개가 남음 + 108개의 쿠폰 생김
# 10 마리를 쿠폰으로 시킬 수 있고 쿠폰 9개가 남음 + 10개의 쿠폰 생김
# 1마리를 쿠폰으로 시킬 수 있고 쿠폰 9개가 남음 + 1개의 쿠폰 생김
# 1마리를 쿠폰으로 시킬 수 있음

def solution(chicken):
    answer = 0
    coupon = 0
    answer = answer + chicken // 10
    coupon = answer + (chicken - chicken//10 * 10)
    while coupon // 10 != 0:
        answer = answer + coupon // 10
        coupon = coupon // 10 + (coupon - coupon // 10 * 10)
    return answer

# 마리수
# answer = answer + chicken // 10
# 0 + 108
# 쿠폰수
# coupon = answer + (chicken - chicken//10 * 10)
# 108 + 1
# 마리수
# answer = answer + coupon // 10
# 108 + 10
# 쿠폰수
# coupon = coupon // 10 + (coupon - coupon // 10 * 10)
# 109 // 10 + (109 - 109//10 * 10) = 19
# 마리수
# answer = answer + coupon // 10
# 118 +1
# 쿠폰수
# coupon = coupon // 10 + (coupon - coupon // 10 * 10)
# 1 + (19 - 10) = 10
# 마리수
# answer = answer + coupon // 10
# 119 + 1
