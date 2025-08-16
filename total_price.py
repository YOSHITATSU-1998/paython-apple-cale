import datetime

# 日付と時間を取得
now = datetime.datetime.now()

apple_price = int(input("リンゴの値段を入力してください: "))
quantity_apple = int(input("リンゴの個数を入力してください: "))
banana_price = int(input("バナナの値段を入力してください: "))
quantity_banana = int(input("バナナの個数を入力してください: "))

total_apple = apple_price * quantity_apple
total_banana = banana_price * quantity_banana
total = total_apple + total_banana

# レシート出力
print("\n============================")
print("       お買い上げレシート")
print(f"日時: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print("----------------------------")
print(f"リンゴ    {apple_price}円 × {quantity_apple}個 = {total_apple}円")
print(f"バナナ    {banana_price}円 × {quantity_banana}個 = {total_banana}円")
print("----------------------------")
print(f"合計金額: {total}円")
print("============================")
print("またのお越しをお待ちしております！")
