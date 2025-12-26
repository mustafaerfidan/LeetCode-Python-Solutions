def maxProfit(prices):
    # Şimdiye kadar gördüğümüz en düşük fiyatı saklamak için
    min_price = float('inf')  # Başlangıçta çok büyük bir sayı

    # Şimdiye kadar elde edebileceğimiz en yüksek kar
    max_profit = 0

    # Tüm fiyatları tek tek dolaşıyoruz
    for price in prices:

        # Eğer bu gün fiyat şimdiye kadarki en düşük fiyatsa
        if price < min_price:
            min_price = price  # minimum fiyatı güncelle

        # Eğer bu gün satarsak daha önceki en yüksek kardan daha iyi kar elde edersek
        elif price - min_price > max_profit:
            max_profit = price - min_price  # en yüksek karı güncelle

    # Döngü bitti, elde edilebilecek en yüksek karı döndür
    return max_profit
