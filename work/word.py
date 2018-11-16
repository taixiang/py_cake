from pydocx import PyDocX
import os
from win32com import client
import subprocess


def createDoc():
    html = PyDocX.to_html("test.docx")
    f = open("3.html", 'w', encoding="utf-8")
    f.write(html)
    f.close()


def re_name(dir_path, old_file, new_file):
    os.renames(dir_path + "/" + old_file, dir_path + "/" + new_file)


def re_name1(old_file, new_file):
    word = client.Dispatch("Word.Application")
    doc = word.Documents.Open("D:\\mine\\py\\py_cake\\work\\111.doc")
    doc.SaveAs("D:\\mine\\py\\py_cake\\work\\222.docx", 16)
    doc.Close()
    word.Quit()


re_name1("111.doc", "111.docx")
# createDoc()

# output = subprocess.check_output(["soffice","--headless","--invisible","--convert-to","docx","D:\\mine\\py\\py_cake\\work\\111.doc","--outdir","D:\\mine\\py\\py_cake\\work\\111.docx"])
