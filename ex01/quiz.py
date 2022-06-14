import random
def main():
    q=random.randint(0,2)
    print("問題：")
    print(shutudai(q))
    ans1=input("答えるんだ：")

    if ans1 in kaito[q] == True:
        print("正解")
    else:
        print("出直してこい")

def shutudai(x):
    ques=["サザエの旦那の名前は？",
    "カツオの妹の名前は？",
    "タラオはカツオから見てどんな関係？"]
    return (ques[x])

def kaito(y):
    ans=[["マスオ", "ますお"],
    ["ワカメ", "わかめ"],
    ["甥", "おい", "甥っ子", "おいっこ"]]
    return ans[y]

if __name__ == "__main__":
    # execute only if run as a script
    main()