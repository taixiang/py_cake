from pydocx import PyDocX
import os
from win32com import client

def createDoc():
    html = PyDocX.to_html("111.doc")
    print(html)
    with open("1.html", 'w') as f:
        f.write(html)


def re_name(dir_path, old_file, new_file):
    os.renames(dir_path + "/" + old_file, dir_path + "/" + new_file)


def re_name1(old_file, new_file):
    word = client.Dispatch("Word.Application")
    doc = word.Documents.Open("D:\\mine\\py\\py_cake\\work\\111.doc")
    doc.SaveAs("D:\\mine\\py\\py_cake\\work\\6666.docx")
    doc.Close()
    word.Quit()

re_name1("111.doc", "111.docx")
# createDoc()
