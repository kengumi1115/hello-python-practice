import random

low, high = 1, 10
max_tries = 5

print(f"数字当てゲーム！ {low}〜{high} の中から数字を当ててね（最大 {max_tries} 回まで）")

answer = random.randint(low, high)   # ← anser → answer に修正
tries = 0
guess = None                         # ループ外でも参照できるように初期化

while tries < max_tries:
    raw_input_value = input(f"{tries + 1} 回目の予想は？ ")

    # 入力バリデーション（空文字や非数字を弾く）
    if not raw_input_value.isdigit():
        print("❌ 数字を入力してね（例: 3）")
        continue

    guess = int(raw_input_value)     # ← raw → raw_input_value に修正

    # 範囲チェック（全角の＃ではなく半角 # でコメント）
    if not (low <= guess <= high):
        print(f"❌ {low} から {high} の数字を入力してね")
        continue

    tries += 1

    # 判定
    if guess == answer:
        print(f"🎉 正解！{tries} 回目で当たったよ！")
        break
    elif guess < answer:
        print("🔼 ヒント: もっと大きい数字だよ")
    else:
        print("🔽 ヒント: もっと小さい数字だよ")

# ゲーム終了判定（構文エラー修正: if の条件部にコロンのみ）
if tries >= max_tries and guess != answer:
    print(f"❌ 残念！正解は {answer} でした")
