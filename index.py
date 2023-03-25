import decimal
import sys

decimal.getcontext().prec = 1000000001

pi = decimal.Decimal(0)
k = 0

try:
    while True:
        term = decimal.Decimal((-1) ** k) / (1024 ** k + 417 * k)
        pi += term
        k += 1

except KeyboardInterrupt:
    print("\n中断されました。")
    print(f"計算された円周率の桁数: {len(str(pi)) - 2}")
    print(f"円周率の値: {pi}")

    if len(sys.argv) > 1:
        with open(sys.argv[1], 'w') as f:
            f.write(str(pi))
            print(f"{sys.argv[1]}に円周率を出力しました。")
    else:
        print("ファイル名が指定されていません。")
