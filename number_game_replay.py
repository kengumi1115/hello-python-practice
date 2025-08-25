import random

LOW, HIGH = 1, 10
MAX_TRIES = 5

def play_once():
    """1回分のゲームを実行して、当たったら True、当たらなければ False を返す"""
    answer = random.randint(LOW, HIGH)
    tries = 0
    guess = None

    print(f"\n数字当てゲーム！ {LOW}〜{HIGH} の中から数字を当ててね（最大 {MAX_TRIES} 回）")

    while tries < MAX_TRIES:
        raw = input(f"{tries + 1} 回目の予想は？ ")

        # 入力チェック：整数か？
        if not raw.isdigit():
            print("⚠ 数字を入力してね（例: 3）")
            continue

        guess = int(raw)

        # 範囲チェック
        if not (LOW <= guess <= HIGH):
            print(f"⚠ {LOW}〜{HIGH} の範囲で入力してね")
            continue

        tries += 1

        if guess == answer:
            print(f"🎉 正解！{tries} 回目で当たったよ！")
            return True
        elif guess < answer:
            print("🔺 ヒント: もっと大きい数だよ")
        else:
            print("🔻 ヒント: もっと小さい数だよ")

    print(f"❌ 残念！正解は {answer} でした")
    return False


def ask_retry():
    """再戦するかを y/n で聞いて、True/False を返す（入力バリデーション付き）"""
    while True:
        ans = input("もう一度遊ぶ？（y/n）: ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("⚠ y か n で答えてね")


def main():
    while True:
        play_once()
        if not ask_retry():
            print("👋 遊んでくれてありがとう！またね")
            break


if __name__ == "__main__":
    main()
