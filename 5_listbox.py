from tkinter import *

root = Tk()
root.title("ClockMakerChoi")
root.geometry("640x480") #가로 * 세로

#selectmode = "single"
listbox1 = Listbox(root, selectmode="single", height=0)
listbox1.insert(0, "사과")
listbox1.insert(1, "딸기")
listbox1.insert(2, "바나나")
listbox1.insert(END, "수박")
listbox1.insert(END, "포도")
listbox1.pack()

#selectmode = "extended"
listbox2 = Listbox(root, selectmode="extended", height=0)
listbox2.insert(0, "사과")
listbox2.insert(1, "딸기")
listbox2.insert(2, "바나나")
listbox2.insert(END, "수박")
listbox2.insert(END, "포도")
listbox2.pack()

#height = n
listbox3 = Listbox(root, selectmode="extended", height=3)
listbox3.insert(0, "사과")
listbox3.insert(1, "딸기")
listbox3.insert(2, "바나나")
listbox3.insert(END, "수박")
listbox3.insert(END, "포도")
listbox3.pack()

def btncmd():
    # 삭제
    #listbox1.delete(END)  #맨 뒤 항목을 삭제
    #listbox1.delete(0)  #맨 앞 항목을 삭제

    # 갯수 확인
    #print("리스트에는", listbox1.size(), "개가 있어요")
    #print("리스트에는", listbox2.size(), "개가 있어요")
    #print("리스트에는", listbox3.size(), "개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    #print("1번째부터 3번째까지의 항목 : ", listbox1.get(0,2))

    # 선택된 항목 확인
    print("선택된 항목 : ", listbox1.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()