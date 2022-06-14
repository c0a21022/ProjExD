import random
import datetime
from sre_constants import CATEGORY_UNI_NOT_LINEBREAK

count=10
mcount=2
replay=5

alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def main():
    st = datetime.datetime.now()

    for i in range(replay):
        question()
        answer()
        


    ed = datetime.datetime.now()
    print("経過時間：" + str((ed-st).seconds) + "秒")

def question():
    ques=[]
    miss=[]
    for i in range(count):
        ques.append(alphabet[random.randint(0,25)])

    print("対象文字：")
    print(*ques)
    
    for i in range(mcount):
        miss.append(ques.pop(random.randint(0,len(ques)-1)))

    print("欠損文字：")
    print(*miss)
    print("表示文字：")
    print(*ques)

def answer():
    mcountans=input("欠損文字はいくつあるでしょうか？：")
    if (mcountans == mcount):
        print("正解です。それでは具体的に欠損文字を1つずつ入力してください")
        miss1=input("1つ目の文字を入力してください")
        miss2=input("2つ目の文字を入力してください")
        if miss1 in miss == True and miss2 in miss == True:
            print("正解です")
        else :
            print("またチャレンジしてください")
    else:
        print("不正解です")

if __name__ == "__main__":
    main()