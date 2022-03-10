#보통 python에서 입력을 받을 때 input()함수를 사용
#빠른 입력을 원하는 경우
import sys
sys.stdin.readline() #이 경우, 입력할 때 맨끝의 줄바꿈 문자(\n)까지 입력이 된다.

sys.stdin.readline().rstrip() #rstrip()을 사용하면 줄바꿈 문자를 제외하고 입력받는다.

x, y = sys.stdin.readline().rsplit() #rsplit()을 사용하면 여러개의 입력을 받을 수 있다.
