import random

kaisuu = 2
mozimax= 10
kesun = 4

def main():

    for _ in range(kaisuu):
        seikai = taisyou()
        a = kaitou(seikai)
        if a == 1:
            print("おめでとう")
            break
        else:
            print("もう一度")
def taisyou():
    temp = [chr(c+65) for c in range(26)]
    alpha = random.sample(temp,mozimax)
    print(alpha)
    kesson = random.sample(alpha,kesun)
    mozi = [s for s in alpha if s not in kesson]
    print(mozi)
    return kesson

def kaitou(seikai):
    num = int(input("欠損文字はいくつか:"))
    print(kesun)
    if num != kesun:
        print("不正解")
        return 0
    for i in range(kesun):
        print(f"{i+1}つ目の欠損は？")
        ans = input()
        if ans in seikai:
            print("正解")
        else:
            print("不正解")
            return 0
    else:
        return 1
if __name__ == "__main__":
    main()