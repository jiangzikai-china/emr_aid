#!/usr/bin/env python
# coding: utf-8

# In[19]:

import numpy as np
from tkinter import *

filepath = 'ref_m.csv'
ref = np.loadtxt(filepath,dtype=np.str,delimiter=',',encoding='ansi')
func_m_result = ""

def transform():
    func_m = entry1.get()
    func_m_result = ""
    if v.get() == 0:
        func_m_result = "完善初期康复评定，全面了解患者功能状况和障碍程度以确定康复目标和制定康复治疗计划："
    elif v.get() == 1:
        func_m_result = "完善中期康复评定，评估患者总的功能情况，有无康复效果，分析其原因，并据此调整康复治疗计划："
    elif v.get() == 2:
        func_m_result = "完善末期康复评定，评估患者总的功能状况，评价治疗效果，为重返家庭和社会或做进一步康复治疗的提出建议："
    else:
        text.insert("你这是干啥呢，选一个啊")
    func_name = ref[:,0].tolist()
    func_real = ref[:,v.get()+1].tolist()
    for i in range(ref.shape[0]):
        if func_name[i] in func_m:
            func_m_result = func_m_result + func_real[i]
        else:
            pass        
    text1.insert("end", func_m_result[:-1]+"；")

root_root = Tk()
root_root.resizable(width=False, height=False)
#root_root.withdraw()
root = Toplevel()
root.resizable(width=False, height=False)
root.title('康复评定医嘱病程录文本生成辅助器 版本：0.1a 作者：JIANG Zikai')
root_root.destroy()
#entry1 = Entry(root)
#entry1.pack()
background_image = PhotoImage(file="bkgrd.gif") 
background_label = Label(root, image=background_image) 
background_label.place(x=0, y=0, relwidth=1, relheight=1) 
v = IntVar()
radio0 = Radiobutton(root,background = 'white',
                     variable = v,
                     value = 0,
                     text='初评')
radio0.pack()
radio1 = Radiobutton(root,background = 'white',
                     variable = v,
                     value = 1,
                     text='中评/周转')
radio1.pack()
radio2 = Radiobutton(root,background = 'white',
                     variable = v,
                     value = 2,
                     text='末评')
radio2.pack()
entry1 = Entry(root)
entry1.place(width=800, height=512) 
entry1.pack()
label1 = Label(root,background = 'white',text="把EMR系统里的评定医嘱全选插入，原始文本贴在上面那个框里")
label1.pack()
button1 = Button(root, background = 'green', text="然后点这里", command=transform)
button1.pack()
text1 = Text(root)
text1.place(width=800, height=768) 
text1.pack()
label2 = Label(root,background = 'white',
               text= "生成的文本还是要稍微看一看改一改的,本人不对生成的任何文本语义负责"
               +"\r\n"+"参照原文件可自添ref_m.csv文件项目，注意中英文标点差异/勿随意更改文件编码格式(ansi)"
               +"\r\n"+"第一列为项目名称，后三列为初中末评文本"
               +"\r\n"+"有事加微信↓")
label2.pack()
wechat = PhotoImage(file="skull.gif")
label3 = Label(root, width=128, height=128, image = wechat, compound = CENTER)
label3.pack()
root.mainloop()



# In[ ]: