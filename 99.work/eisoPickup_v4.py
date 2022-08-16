"""
20220418: nishikiori

[使い方]
（１）各定数の値を確認し、必要に応じて書き換える
（２）下記コマンドで実行
Windows: # py eisoPickup.py {処理対象ディレクトリパス}
Ubuntu:  # python3 eisoPickup.py {処理対象ディレクトリパス}

[概要]
特定のタグを含むjsonファイルを探索する。
結果（パスのリスト）はtxtに出力し、フラグによってはファイルのコピーも行う。
コピーするのは「元画像＆json」のみで、分割後のファイルは対象外となる。

結果ディレクトリ内には2つか3つのディレクトリが作成される。
crop: 分割を行う元画像・json
not_crop: 分割を行わない元画像・json
other: タグが見つからなかった元画像・json。
       不要なら「FLAG_NOT_FOUND_COPY」をFalseにしておくと処理時間が大幅に短くなる。
"""

import os
import sys
import time
import glob
# from PIL import Image
import shutil
import json

from pyparsing import traceback


# 結果を格納するディレクトリ。プログラム実行時のカレント以下に作成される
RESULT_DIR = 'results'

# 対象のjsonファイルをRESULT_DIRにコピーするかどうか
FLAG_COPY = True

# 対象のタグが含まれていないファイルをotherディレクトリにコピーするかどうか
FLAG_NOT_FOUND_COPY = True

# 検索対象のタグ名
SEARCH_TAG = 'cable'


def create_dir():
    """
    結果を格納する次の5つのディレクトリを作成する。
    ./{RESULT_DIR}　* 存在しない場合のみ
    ./{RESULT_DIR}/{unixtime}_{SEARCH_TAG}_Pickup
    ./{RESULT_DIR}/{unixtime}_{SEARCH_TAG}_Pickup/crop
    ./{RESULT_DIR}/{unixtime}_{SEARCH_TAG}_Pickup/not_crop
    ./{RESULT_DIR}/{unixtime}_{SEARCH_TAG}_Pickup/other

    Returns:
        str: 作成されたディレクトリのパス
    """
    # {current}/results/{unixtime}
    timestamp = round(time.time())
    new_dir_path = os.path.join(os.path.abspath('.'), RESULT_DIR, f'{str(timestamp)}_{SEARCH_TAG}_Pickup')
    os.makedirs(new_dir_path, exist_ok=True)

    result_dir_crop = os.path.join(new_dir_path, 'crop')
    result_dir_not_crop = os.path.join(new_dir_path, 'not_crop')
    result_dir_other = os.path.join(new_dir_path, 'other')
    os.makedirs(result_dir_crop)
    os.makedirs(result_dir_not_crop)
    if FLAG_NOT_FOUND_COPY:
        os.makedirs(result_dir_other)
    print(f'保存先フォルダを作成しました: {new_dir_path}')
    return new_dir_path


def main():
    s_time = time.time()
    args = sys.argv
    if len(args) < 2:
        print('検索対象のフォルダのパスを指定してください')
        sys.exit()
    target_path = args[1]

    # 引数に渡したパスがフォルダかのチェック
    if os.path.isdir(target_path):
        # タグ情報ファイルのリストを取得（crop2も含む）
        json_paths = [
            filename for filename in glob.iglob(os.path.join(target_path, '*.json'))
        ]
    else:
        print('指定されたパスはフォルダではありません')
        sys.exit()

    # jsonリストが空の場合は終了
    if not json_paths:
        print('タグ情報ファイルが見つかりませんでした')
        sys.exit()

    print(f'[DEBUG] len(json_paths): {len(json_paths)}')
    
    # 結果格納ディレクトリを作成
    result_dir = create_dir()

    # 分割しないもの
    target_json_paths1 = []
    result_dir_not_crop = os.path.join(result_dir, 'not_crop')
    # 分割するもの
    target_json_paths2 = []
    result_dir_crop = os.path.join(result_dir, 'crop')
    # 指定のタグを含まないもの
    other_json_paths = []
    result_dir_other = os.path.join(result_dir, 'other')
    # 画像とjsonが揃っていないもの
    err_json_paths = []

    for json_path in json_paths:
        # jsonファイルに指定のタグが含まれているかを検索
        with open(json_path, 'r') as f:
            data = json.load(f)
            basename = os.path.basename(json_path)
            splitext = os.path.splitext(basename)

            search_flag = False
            if "detection" in data:
                data = data["detection"]
            for tmp in data:
                if "classification" in data:
                    break
                if tmp.get('class') == SEARCH_TAG:
                    search_flag = True

                    # 指定のタグが含まれていても、分割されたタグ情報ファイルの場合は何もしない
                    if 'crop2' in basename:
                        break

                    # 対象の元画像から作られた分割ファイルのパスリストが存在するかを確認する
                    crop2_json_paths = [
                        filename for filename in glob.glob(os.path.join(target_path, f'{splitext[0]}.crop2*'))
                    ]

                    # 実際にコピーするファイルのパスリストを作成（元画像と元タグ情報ファイル）
                    copy_paths = [
                        filename for filename in glob.glob(os.path.join(target_path, f'{splitext[0]}.*'))
                        if 'crop2' not in filename
                    ]

                    if len(copy_paths) < 2:
                        print(f'ファイルが不足しているため処理をスキップします: {json_path}')
                        print(copy_paths)
                        err_json_paths.append(os.path.basename(json_path))
                        break

                    if len(copy_paths) != 2:
                        print(f'ファイル数に異常があるため処理をスキップします: {json_path}')
                        print(copy_paths)
                        break

                    if crop2_json_paths:
                        # 分割対象
                        target_json_paths1.append(os.path.basename(json_path))
                        # フラグが設定されている場合はコピーする
                        if FLAG_COPY:
                            for copy_path in copy_paths:
                                shutil.copy(copy_path, result_dir_crop)
                            for copy_path_crop2 in crop2_json_paths:
                                shutil.copy(copy_path_crop2, result_dir_crop)
                    else:
                        # 分割対象でない
                        target_json_paths2.append(os.path.basename(json_path))
                        # フラグが設定されている場合はコピーする
                        if FLAG_COPY:
                            for copy_path in copy_paths:
                                shutil.copy(copy_path, result_dir_not_crop)
                    # 一つ見つかったら次のファイルの処理へ移行する
                    break

            # ここに至る＝指定のタグが含まれていないということ
            # 分割有無に関わらずすべてotherディレクトリにコピーする
            if not search_flag:
                if FLAG_NOT_FOUND_COPY:
                    other_json_paths.append(os.path.basename(json_path))
                    if FLAG_COPY:
                        # 実際にコピーするファイルのパスリストを作成（画像とタグ情報ファイルのセット）
                        copy_paths = [
                            filename for filename in glob.glob(os.path.join(target_path, f'{splitext[0]}.*'))
                        ]
                        if len(copy_paths) < 2:
                            print(f'ファイルが不足しているため処理をスキップします: {json_path}')
                            print(copy_paths)
                            err_json_paths.append(os.path.basename(json_path))
                            continue
                        for copy_path in copy_paths:
                            shutil.copy(copy_path, result_dir_other)

    # 結果をテキストファイルに出力する
    with open(os.path.join(result_dir, f'{SEARCH_TAG}_json_crop.txt'), 'w') as f:
        for d in target_json_paths1:
            f.write("%s\n" % d)
    with open(os.path.join(result_dir, f'{SEARCH_TAG}_json_not_crop.txt'), 'w') as f:
        for d in target_json_paths2:
            f.write("%s\n" % d)
    if FLAG_NOT_FOUND_COPY:
        with open(os.path.join(result_dir, f'{SEARCH_TAG}_json_other.txt'), 'w') as f:
            for d in other_json_paths:
                f.write("%s\n" % d)
    with open(os.path.join(result_dir, 'err_json.txt'), 'w') as f:
        for d in err_json_paths:
            f.write("%s\n" % d)

    end = time.time() - s_time
    print(f'\n所要時間: {end} sec')


main()
