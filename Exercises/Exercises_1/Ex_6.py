# write a program that read article price excluding tax, number of articles and VAT rate, than calc TTC
ht = float(input("Enter Article price: "))
nbArticle = int(input("Enter number of articles: "))
tva = float(input("Enter VAT: "))

ttc = (ht * nbArticle) * (1 + (tva / 100))

print(f"TTC = {ttc}")
