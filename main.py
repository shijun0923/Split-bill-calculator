class Member:
    # 建構子
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def __str__(self):
        return f"{self.name}的淨餘額為: {self.balance}"
    

# 處理記帳與更新淨餘額
def add_expense(group, payer, total, split_among):
    """
    group: 裝有所有成員物件的字典
    payer: 字串，付款人的名字
    total: 數字，總花費金額
    split_among: 陣列 (List)，裝著需要分攤這筆錢的人名
    """

    # 步驟 1：算出每個人平均要分攤多少錢 (用總金額除以分攤人數)
    average = total / len(split_among)

    # 步驟 2：幫「付款人」的餘額加上總金額 (代表大家欠他這些錢)
    group[payer].balance += total

    # 步驟 3：把「要分攤這筆錢的人」，每個人的餘額都扣掉平均費用
    for name in split_among:
        group[name].balance -= average


# 處理記帳與更新淨餘額
def settle_debts(group):
    payers = []     # 裝餘額小於 0 的 Member 物件
    receivers = []  # 裝餘額大於 0 的 Member 物件

    # 直接走訪字典的 Value
    # 可以直接略過「查字典」這個動作
    for obj in group.values():
        if obj.balance < 0:
            payers.append(obj)
        elif obj.balance > 0:
            receivers.append(obj)

    # 只要名單裡還有人，就繼續結算
    while payers and receivers:
        p = payers[0]
        r = receivers[0]

        # 1. 決定這次要轉多少錢 (p.balance 取絕對值後，與 r.balance 比大小，取小的)
        amount = min(abs(p.balance), r.balance)

        # 2. 印出轉帳明細
        print(f"{p.name} 要給 {r.name} {amount} 元")

        # 3. 更新餘額
        p.balance += amount
        r.balance -= amount

        # 4. 判斷是否結清，如果餘額為 0 就把他從陣列中踢掉
        if p.balance == 0:
            payers.pop(0)
        if r.balance == 0:
            receivers.pop(0)


if __name__ == "__main__":          #「只有當我直接執行這支檔案時，才執行以下區塊」
    # Key: 名字 (字串，用來快速尋找)
    # Value: Member 實體物件 (裝載該成員的狀態與功能)
    group = {}

    group["仕均"] = Member("仕均")
    group["宗澤"] = Member("宗澤")
    group["華葦"] = Member("華葦")
    group["子祁"] = Member("子祁")
    group["柚子"] = Member("柚子")

    print("開始分帳！")
    while True:
        print("\n選擇動作：")
        print("1: 新增一筆花費")
        print("2: 結算所有帳務並離開")
        print("3: 查看目前所有人餘額")

        # input() 接收到的所有東西，在 Python 裡都會被當成字串
        choice = input("輸入選項 (1,2,3): ")

        if choice == "1":
            payer = input("付款人: ")
            total_str = input("總金額: ")

            # 處理金額型別轉換
            total = int(total_str)

            # 格式要絕對正確 !!!
            split_str = input("輸入分攤人名字 (用逗號分隔:仕均,宗澤): ")

            # 處理字串切割
            split_among = split_str.split(",")

            # 呼叫記帳函式
            add_expense(group,payer,total,split_among)
            print("記帳成功！")

        elif choice == "2":
            print("\n--- 最終轉帳明細 ---")
            settle_debts(group)
            break

        elif choice == "3":
            print("\n--- 目前帳務狀況 ---")
            for obj in group.values():
                print(obj)
        
        else:
            print("輸入錯誤，請重新輸入")
