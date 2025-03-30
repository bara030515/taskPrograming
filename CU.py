import tkinter
import tkinter.font
root = tkinter.Tk()

# 총 매출액 걔산 출력 함수
def click_calculation():
    # 물품 수량 변수    
    countCoffee_Sell = int(entry1_1.get())
    countSamkim_Sell = int(entry1_2.get())
    countBanana_Sell = int(entry1_3.get())
    countLunchs_Sell = int(entry1_4.get())
    countCokela_Sell = int(entry1_5.get())
    countSnacks_Sell = int(entry1_6.get())

    countCoffee_Cost = int(entry2_1.get())
    countSamkim_Cost = int(entry2_2.get())    
    countBanana_Cost = int(entry2_3.get())    
    countLunchs_Cost = int(entry2_4.get())    
    countCokela_Cost = int(entry2_5.get())    
    countSnacks_Cost = int(entry2_6.get()) 


    # 총 매출출액 계산
    total = 0

    total += countCoffee_Sell * 1800
    total += countSamkim_Sell * 1400
    total += countBanana_Sell * 1800
    total += countLunchs_Sell * 4000
    total += countCokela_Sell * 1500
    total += countSnacks_Sell * 2000

    total -= countCoffee_Cost * 500
    total -= countSamkim_Cost * 900
    total -= countBanana_Cost * 800
    total -= countLunchs_Cost * 3500
    total -= countCokela_Cost * 700
    total -= countSnacks_Cost * 1000


    str1 = '오늘 총 매출액은 ' + str(total) + '원 입니다.'
    labelRes = tkinter.Label(root, text=str1, font=('돋움', 10))
    labelRes.place(x=100, y=200)

# 화면 설정
root.title('CU')
root.geometry('600x250')

# 항목 라벨
lbSell = tkinter.Label(root, text='판매 수량', font=('돋움',10))
lbCost = tkinter.Label(root, text='구매 수량', font=('돋움',10))
coffee = tkinter.Label(root, text='캔 커피', font=('돋움',10))
samkim = tkinter.Label(root, text='삼각김밥', font=('돋움',10))
banana = tkinter.Label(root, text='바나나 우유', font=('돋움',10))
lunchs = tkinter.Label(root, text='도시락', font=('돋움',10))
cokela = tkinter.Label(root, text='콜라', font=('돋움',10))
snacks = tkinter.Label(root, text='새우깡', font=('돋움',10))

lbSell.place(x=10, y=70)
lbCost.place(x=10, y=120)
coffee.place(x=70, y=25)
samkim.place(x=152, y=25)
banana.place(x=227, y=25)
lunchs.place(x=328, y=25)
cokela.place(x=417, y=25)
snacks.place(x=497, y=25)

# 수량 입력칸 설정
entry1_1 = tkinter.Entry(width=5)
entry1_2 = tkinter.Entry(width=5)
entry1_3 = tkinter.Entry(width=5)
entry1_4 = tkinter.Entry(width=5)
entry1_5 = tkinter.Entry(width=5)
entry1_6 = tkinter.Entry(width=5)

entry1_1.place(x=75, y=70)
entry1_2.place(x=160, y=70)
entry1_3.place(x=245, y=70)
entry1_4.place(x=330, y=70)
entry1_5.place(x=415, y=70)
entry1_6.place(x=500, y=70)


entry2_1 = tkinter.Entry(width=5)
entry2_2 = tkinter.Entry(width=5)
entry2_3 = tkinter.Entry(width=5)
entry2_4 = tkinter.Entry(width=5)
entry2_5 = tkinter.Entry(width=5)
entry2_6 = tkinter.Entry(width=5)

entry2_1.place(x=75, y=120)
entry2_2.place(x=160, y=120)
entry2_3.place(x=245, y=120)
entry2_4.place(x=330, y=120)
entry2_5.place(x=415, y=120)
entry2_6.place(x=500, y=120)

# 계산 버튼
calculation = tkinter.Button(root, text='계산', font=('돋움', 10), command=click_calculation)
calculation.place(x=50, y= 160, width=500)

root.mainloop()
