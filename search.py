import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word, csv_save):
    # 検索対象取得
    df=pd.read_csv("./{}".format(csv_save))
    source=list(df["name"])

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        return "『{}』はあります".format(word)
    else:
        print("『{}』はありません。{}を追加します".format(word, word))
        source.append(word)
        df = pd.DataFrame(source, columns=['name'])
        df.to_csv('./{}'.format(csv_save), encoding='utf-8')
        return "『{}』はありません。{}を追加します".format(word, word)
        
    
    
    