import sys

input = sys.stdin.readline

x=int(input())
n=int(input())
k=0
for i in range(n):
    a,b=map(int, input().split())
    k+=(a*b)

print("Yes" if k==x else "No")
