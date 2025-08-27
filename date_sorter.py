import os
import sys
import shutil
import datetime

DRY_RUN = True  # Trueの間は実際には移動しません。動作確認後にFalseにしてください。
default_target = r"C:\Users\sasuk\OneDrive\デスクトップ\AWS\portfolio"

def yyyymm_from_mtime(path: str) -> str:
    ts = os.path.getmtime(path)
    dt = datetime.datetime.fromtimestamp(ts)
    return f"{dt.year:04d}-{dt.month:02d}"

def safe_move(src_path: str, dst_dir: str, file_name: str) -> str:
    os.makedirs(dst_dir, exist_ok=True)
    name, ext = os.path.splitext(file_name)
    candidate = os.path.join(dst_dir, file_name)
    counter = 1
    while os.path.exists(candidate):
        candidate = os.path.join(dst_dir, f"{name}_{counter}{ext}")
        counter += 1

    if DRY_RUN:
        print(f"[DRY RUN] MOVE: {src_path} -> {candidate}")
    else:
        shutil.move(src_path, candidate)
        print(f"MOVED    : {src_path} -> {candidate}")
    return candidate

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else default_target
    target = os.path.abspath(target)

    if not os.path.isdir(target):
        print(f"× フォルダが見つかりません: {target}")
        sys.exit(1)

    print(f"📂 対象フォルダ: {target}")
    print(f"🔒 DRY_RUN = {DRY_RUN} (Trueの間は移動しません)\n")

    this_file = os.path.basename(__file__)

    for entry in os.listdir(target):
        src_path = os.path.join(target, entry)

        if os.path.isdir(src_path):
            continue

        if entry == this_file:
            continue

        yyyymm = yyyymm_from_mtime(src_path)
        dst_dir = os.path.join(target, yyyymm)
        safe_move(src_path, dst_dir, entry)

    print("\n✅ 完了（DRY_RUN=True のままなら、まだ何も移動していません）")
    print("👉 実際に移動するには DRY_RUN を False にして再実行してね。")

if __name__ == "__main__":
    main()
