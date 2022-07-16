# ch17_13.py
import docx

wdoc = docx.Document()
table = wdoc.add_table(rows=2, cols=2)
row = table.rows[0]
row.cells[0].text = '書號'
row.cells[1].text = '我的著作'
row = table.rows[1]
row.cells[0].text = 'XA1711'
row.cells[1].text = 'HTML5+CSS3王者歸來'
# 增加表格行和輸入資料
new_row = table.add_row()                   # 增加表格行          
new_row.cells[0].text = 'XA1774'
new_row.cells[1].text = 'Python王者歸來'
table.style = 'LightShading-Accent1'        # 設定表格樣式
wdoc.save('out17_13.docx')


