import eel
import desktop
import search
import pandas as pd

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def kimetsu_search(word, csv_save): # 検索ワードを元にCSVファイル内を検索して結果をhtmlに返す
    return search.kimetsu_search(word, csv_save)
    
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)