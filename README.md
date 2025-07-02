# Taiwan Nightmarket Snacks Django Project

Django應用程式，列出台灣前20有名的夜市美食、所在城市、所在夜市。

## 功能
- 模型：美食名稱、所在城市、所在夜市。
- 資料：20筆美食名稱、21筆所在城市、20所在夜市。
- 網頁：`http://127.0.0.1:8000/`。

按照功課要求做以下動作，所需要指令

## 資料測試
1. 匯出資料：
   python manage.py dumpdata > data.json

2. 格式化資料集：
   python manage.py dumpdata --indent 2 > data.json

3. 清理原始資料：
   python manage.py flush

4. 匯入資料：
   python manage.py loaddata data.json   
   驗證：訪問http://127.0.0.1:8000/
   應顯示20筆夜市美食。
