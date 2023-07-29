def count_sellers_and_buyers(apple_price, sellers, buyers):
    sellers_count = 0
    buyers_count = 0

    for price in sellers:
        if price >= apple_price:
            sellers_count += 1

    for price in buyers:
        if price <= apple_price:
            buyers_count += 1

    return sellers_count, buyers_count

def binary_search_lowest_price(sellers, buyers):
    # 売り手と買い手の価格リストをソート
    sellers.sort()
    buyers.sort()

    # 価格の範囲を取得
    lowest_price = sellers[0]
    highest_price = buyers[-1]

    # 二分探索で条件を満たす最小の価格を探索
    result_price = None
    while lowest_price <= highest_price:
        mid_price = (lowest_price + highest_price) // 2
        sellers_count, buyers_count = count_sellers_and_buyers(mid_price, sellers, buyers)

        if sellers_count >= buyers_count:
            result_price = mid_price
            highest_price = mid_price - 1
        else:
            lowest_price = mid_price + 1

    return result_price

# 入力例を使ってテスト
N, M = map(int, input().split())
sellers = list(map(int, input().split()))
buyers = list(map(int, input().split()))
result = binary_search_lowest_price(sellers, buyers)
print(result)  # 出力結果は5
