import time
meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL" : "Tanggapan terhadap lelucon",
            "SHEESH" : "Sedikit ketidaksetujuan",
            "CREEPY" : "Menakutkan, tidak menyenangkan",
            "AGGRO" : "Untuk menjadi agresif/marah",
            }
for i in range(5):
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    if word in meme_dict.keys():
        # Apa yang harus kita lakukan jika kata itu ditemukan?
        arti = meme_dict[word]
        print(arti)
        time.sleep(1)
    else:
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
        print("TIDAK DITEMUKAN")
        time.sleep(1)
