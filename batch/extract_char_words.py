'''
Created on 2018/11/23

@author: hatamasa
'''
import os
import chardet

# 元テキスト抽出力クラス
class ExtractCharWords:
    readdir = '../library/input'
    outdir = '../library'
    outpurt_char_name = 'シンジ'

    def __init__(self):
        '''
        Constructor
        '''

    def execute(self):
        print('readdir: ' + self.readdir)
        print('outdir: ' + self.outdir)
        # 配下のファイル読み込み
        txts = os.listdir(self.readdir)
        # ファイルごとにループ
        for txt in txts:
            # txt拡張子以外無視
            if not (txt.split(".")[-1] == "txt"):
                continue
            # 相対パスを作成
            txt = os.path.join(self.readdir, txt)

            if os.path.isfile(txt):
                print(txt)
            else:
                print("ファイルがありません")
                return

            fp = open(txt, "rb")

            for line in fp:
                # ファイルの文字コード取得
                f_encode = chardet.detect(line)["encoding"]
                # unicode変換
                line_u = str(line, f_encode)

                # キャラ名を取得
                if line_u.find(u"(", 0) == 0:
                    char_name = line_u[line_u.find(u"(") + 1:line_u.find(u"「")]
                else:
                    char_name = line_u[:line_u.find(u"「")]
                # 取得するキャラ名以外はスルー
                if char_name != self.outpurt_char_name:
                    continue

                outfname = os.path.join(self.outdir, char_name + ".txt")
                # キャラ名のファイルがある場合は追記、ない場合は新規作成
                if os.path.exists(outfname):
                    outfp = open(outfname, "a")
                else:
                    outfp = open(outfname, "w")

                # セリフ抽出
                line_format = line_u[line_u.find(u"「") + 1:line_u.find(u"」")] + "\n"
                # セリフ書き込み
                outfp.write(line_format)


extractCharWords = ExtractCharWords()
extractCharWords.execute()