# 18014 A+B Problem
# https://www.acmicpc.net/problem/18014
# Gold 4
# solved

import sys
import time

def solve(N, A, M, B):
  A.reverse()
  B.reverse()
  
  res = []
  carry = 0
  pA = 0
  pB = 0
  
  # 두 숫자의 블록을 하나씩 소모하며 계산
  while pA < N or pB < M or carry:
    # 1. 현재 블록의 숫자와 남은 길이 파악
    lenA = A[pA][0] if pA < N else 0
    dA = A[pA][1] if pA < N else 0
    lenB = B[pB][0] if pB < M else 0
    dB = B[pB][1] if pB < M else 0
    
    # 2. 처리할 공통 길이 L 결정
    if lenA > 0 and lenB > 0: L = min(lenA, lenB)
    elif lenA > 0: L = lenA
    elif lenB > 0: L = lenB
    else: L = 0
    
    if L > 0:
      s = dA + dB + carry
      # 올림수가 변하지 않고 일정하게 유지되는 구간인지 판단
      # s=9인 경우 carry에 따라 다음 자리 숫자가 결정되므로 블록 전체가 동일 결과
      if dA + dB != 9:
        # dA+dB가 9가 아니면 첫 칸 이후 carry는 고정됨
        # 첫 번째 칸 처리
        first_digit = s % 10
        new_carry = s // 10
        
        if res and res[-1][1] == first_digit: res[-1][0] += 1
        else: res.append([1, first_digit])
        
        # 나머지 L-1 칸 처리 (이 구간은 carry가 new_carry로 고정됨)
        if L > 1:
          mid_s = dA + dB + new_carry
          mid_digit = mid_s % 10
          new_carry = mid_s // 10 # 9가 아니므로 변하지 않음
          
          if res and res[-1][1] == mid_digit: res[-1][0] += (L - 1)
          else: res.append([L - 1, mid_digit])
        carry = new_carry
      else:
        # dA + dB == 9 인 경우: carry가 그대로 유지되면서 통과됨
        # (9 + 1 = 10 -> digit 0, carry 1 / 9 + 0 = 9 -> digit 9, carry 0)
        digit = s % 10
        if res and res[-1][1] == digit: res[-1][0] += L
        else: res.append([L, digit])
        # carry는 변하지 않고 유지됨 (s//10 == carry)
    
    elif carry: # 남은 블록은 없는데 carry만 있는 경우
      if res and res[-1][1] == carry: res[-1][0] += 1
      else: res.append([1, carry])
      carry = 0
    
    # 3. 소모한 길이만큼 차감
    if pA < N:
        A[pA][0] -= L
        if A[pA][0] == 0: pA += 1
    if pB < M:
        B[pB][0] -= L
        if B[pB][0] == 0: pB += 1

  # 결과 출력 양식 맞추기
  res.reverse()
  
  # 선행 0 제거 (결과가 0인 경우 제외)
  while len(res) > 1 and res[0][1] == 0:
    res.pop(0)
  
  print(len(res))
  for t, d in res:
    print(f"{t} {d}")

def main():
  data = sys.stdin.read().strip().split()
  K = int(data[0]); data = data[1:]
  for k in range(1, K+1):
    N = int(data[0]); data = data[1:]
    A = [[int(data[2*i]), int(data[2*i+1])] for i in range(N)]; data = data[2*N:]
    M = int(data[0]); data = data[1:]
    B =  [[int(data[2*i]), int(data[2*i+1])] for i in range(M)]; data = data[2*M:]
    
    print(f"Data Set {k}:")
    solve(N, A, M, B)
    print()
  

if __name__ == "__main__":
  main()