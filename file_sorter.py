import os
import shutil
import sys

# ========== 設定 ==========
DRY_RUN = True  # True の間は「シミュレーションのみ」で移動しない
default_target = r"C:\Users\sasuk\OneDrive\デスクトップ\AWS\portfolio"
# ===========================


def safe_move(src_path: str, dst_dir: str, filename: str) -> str:
    """
    ファイルを安全に移動する関数
    - 移動先フォルダがなければ作成
    - 同名ファイルがあれば _1, _2 と連番を付与
    - DRY_RUN=True のときは「計画だけ表示」
    """
    os.makedirs(dst_dir, exist_ok=True)  # フォルダを作成（存在していれば何もしない）
    name, ext = os.path.splitext(filename)
    candidate = os.path.join(dst_dir, filename)
    counter = 1

    # 同名ファイルがあれば連番を付けて回避
    while os.path.exists(candidate):
        candidate = os.path.join(dst_dir, f"{name}_{counter}{ext}")
        counter += 1

    # DRY_RUN に応じて処理
    if DRY_RUN:
        print(f"[DRY RUN] MOVE: {src_path} -> {candidate}")
    else:
        shutil.move(src_path, candidate)
        print(f"MOVED    : {src_path} -> {candidate}")

    return candidate


def main():
    """
    メイン処理
    - 対象フォルダを決定（引数があれば優先、なければデフォルト）
    - フォルダ内のファイルを走査し、拡張子ごとにフォルダ分けして safe_move で移動
    """
    target = sys.argv[1] if len(sys.argv) > 1 else default_target
    target = os.path.abspath(target)

    if not os.path.isdir(target):
        print(f"× フォルダが見つかりません: {target}")
        sys.exit(1)

    print(f"📂 対象フォルダ: {target}")
    print(f"🔒 DRY_RUN = {DRY_RUN}（True の間は移動しません）\n")

    this_file = os.path.basename(__file__)

    for entry in os.listdir(target):
        src_path = os.path.join(target, entry)

        # フォルダは対象外
        if os.path.isdir(src_path):
            continue

        # 自分自身は移動しない
        if entry == this_file:
            continue

        # 拡張子から移動先フォルダを決定
        name, ext = os.path.splitext(entry)
        if ext:
            subdir = ext.lstrip(".").lower()
        else:
            subdir = "no_ext"

        dst_dir = os.path.join(target, subdir)
        safe_move(src_path, dst_dir, entry)

    print("\n✅ 完了（DRY_RUN=True のままなら、まだ何も移動していません）")
    print("👉 実際に移動するには DRY_RUN を False にして再実行してください。")


if __name__ == "__main__":
    main()
