import MeCab
from ai.markov import Markov

class MakeSentence:
    fpath = 'library/シンジ.txt'

    # 文言を作成して返却する
    def generate_sentence(self, input_text):
        import_text = open(self.fpath, "r").read()
        analyzed_text = MeCab.Tagger("-Owakati").parse(import_text).rstrip(" \n").split(" ")
        markov = Markov(analyzed_text)

        # 入力から名詞を抽出
        nouns = []
        for chunk in MeCab.Tagger().parse(input_text).splitlines()[:-1]:
            (surface, feature) = chunk.split('\t')
            if feature.startswith('名詞'):
                nouns.append(surface)

        output_text = markov.answer(nouns)

        if output_text == "":
            output_text = "言っていることがよくわからないなぁ。。。"

        return output_text