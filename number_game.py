import random

# 1〜10 のランダムな数字を生成
answer = random.randint(1, 10)

print("数字当てゲーム！ 1〜10 の中から数字を当ててね")

# ユーザーの入力を数値に変換
guess = int(input("あなたの予想は？ "))

# 判定
if guess == answer:
    print("🎉 正解！すごい！")
else:
    print(f"❌ 残念！正解は {answer} でした")
