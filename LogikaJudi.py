import random
from prompt_toolkit import prompt # type: ignore
from prompt_toolkit.shortcuts import radiolist_dialog # type: ignore

print("🎰 Selamat datang di *Mahjong Ways 1*! 🎲💰")
print("Coba peruntungan Anda dan menangkan hadiah besar!")

def simulate_gambling(initial_deposit, win_probability, rounds, min_deposit_for_win, forced_wins=None):
    balance = initial_deposit
    results = []
    forced_wins = set(forced_wins or [])
    
    for i in range(rounds):
        if balance <= 0:
            print("💸 Saldo habis, permainan berakhir.")
            break
        
        
        print(f"💰 Saldo saat ini: Rp {balance:,.0f}")
        
      
        bet_amount = radiolist_dialog(
            title=f"🎲 Pilih jumlah taruhan untuk putaran {i+1}",
            text=f"Saldo Anda: Rp {balance:,.0f}\nPilih jumlah taruhan Anda:",
            values=[
                (400, "Rp 400"),
                (600, "Rp 600"),
                (800, "Rp 800"),
                (1200, "Rp 1.200"),
                (1400, "Rp 1.400"),
                (1600, "Rp 1.600"),
                (1800, "Rp 1.800"),
                (2000, "Rp 2.000"),
                (4000, "Rp 4.000"),
                (6000, "Rp 6.000"),
                (8000, "Rp 8.000"),
                (10000, "Rp 10.000"),
                (12000, "Rp 12.000"),
                (14000, "Rp 14.000"),
                (16000, "Rp 16.000"),
                (18000, "Rp 18.000"),
                (20000, "Rp 20.000"),
            ]
        ).run()
        
        if bet_amount is None:
            print("⚠️ Taruhan dibatalkan!")
            continue

        if bet_amount > balance:
            print("⚠️ Taruhan melebihi saldo yang tersedia! Taruhan otomatis disesuaikan dengan saldo tersisa.")
            bet_amount = balance
        
        if initial_deposit < min_deposit_for_win:
            balance -= bet_amount
            results.append(f"{i+1}. ❌ Kalah")
        else:
            if (i+1) in forced_wins:
                balance += int(bet_amount * 500) # Kelipatan Menang ( Saldo Terakhir + Bet yang di atur di rounde akan di kalikan 20 sepeti di contoh )
                results.append(f"{i+1}. 🎉 Menang!")
            else:
                balance -= bet_amount
                results.append(f"{i+1}. ❌ Kalah")
        
    
        print(f"💰 Saldo setelah putaran {i+1}: Rp {balance:,.0f}")
    
    return balance, results


initial_deposit = int(input("💵 Masukkan jumlah deposit (Rp): ").replace('.', '').replace(',', ''))


win_probability = 0.4 
rounds = 5  # Atur Berapa Rounde Permainan
min_deposit_for_win = 30000  #Isi dengan Minimal deposit menang misal ( Rp. 30.000)
forced_wins = [1,5,6]  # Disini Bisa Di Atur di Rounde Berapa Kemenangan


final_balance, game_results = simulate_gambling(initial_deposit, win_probability, rounds, min_deposit_for_win, forced_wins)


print("\n🎲 Permainan Selesai! 🎲")
print(f"🏆 Saldo akhir: Rp {final_balance:,.0f}")
print("\n📜 Hasil permainan:")
for result in game_results:
    print(result)
