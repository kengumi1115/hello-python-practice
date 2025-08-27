import os
import shutil
import sys
import datetime

# ===== 設定 =========================================
DRY_RUN = True  # True の間は移動せず「計画」だけ表示
DEFAULT_TARGET = r"C:\Users\sasuk\OneDrive\デスクトップ\AWS\portfolio"
# ====================================================


def yyyymm_from_mtime(path: str) -> str:
    """
    ファイルの最終更新日時 (mtime) から 'YYYY-MM' 文字列を作る。
    例: 2025年8月更新 → '2025-08'
    """
    ts = os.path.getmtime(path)                          # ファイルの更新時刻(UNIX時刻)
    dt = datetime.datetime.fromtimestamp(ts)             # datetime に変換
    return f"{dt.year:04d}-{dt.month:02d}"              # 'YYYY-MM' 形式で返す


def safe_move(src_path: str, dst_dir: str, filename: str) -> str:
    """
    同名衝突を避けて安全に移動する。
    既に同名があれば name_1, name_2 ... と連番付与。
    """
    os.makedirs(dst_dir, exist_ok=True)                  # 移動先フォルダが無ければ作成
    name, ext = os.path.splitext(filename)
    candidate = os.path.join(dst_dir, filename)
    counter = 1
    while os.path.exists(candidate):                     # かぶってたら _1, _2 を付ける
        candidate = os.path.join(dst_dir, f"{name}_{counter}{ext}")
        counter += 1

    if DRY_RUN:
        print(f"[DRY RUN] MOVE: {src_path} -> {candidate}")
    else:
        shutil.move(src_path, candidate)                 # 実際に移動
        print(f"MOVED    : {src_path} -> {candidate}")
    return candidate


def main():
    # 対象フォルダの決定（引数 > デフォルト）
    target = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TARGET
    target = os.path.abspath(target)

    if not os.path.isdir(target):
        print(f"❌ フォルダが見つかりません: {target}")
        sys.exit(1)

    print(f"📂 対象フォルダ: {target}")
    print(f"🔒 DRY_RUN = {DRY_RUN}（True の間は移動しません）\n")

    this_file = os.path.basename(__file__)               # 自分自身は移動しない

    for entry in os.listdir(target):                     # 直下のアイテムを走査
        src_path = os.path.join(target, entry)

        if os.path.isdir(src_path):                      # フォルダはスキップ
            continue
        if entry == this_file:                           # 自分自身はスキップ
            continue

        yyyymm = yyyymm_from_mtime(src_path)            # 例: '2025-08'
        dst_dir = os.path.join(target, yyyymm)          # 移動先: target/YYYY-MM/
        safe_move(src_path, dst_dir, entry)

    print("\n✅ 完了（DRY_RUN=True のままなら、まだ何も移動していません）")
    print("👉 実行移動するには DRY_RUN を False にして再実行してね。")


if __name__ == "__main__":
    main()
