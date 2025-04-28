from eth_account import Account
from web3 import Web3
from colorama import init, Fore, Style

#inisialisasi 
init(autoreset=True)
rpc_url ="https://eth-mainnet.g.alchemy.com/v2/0fryxaVx5cQObGD-HbvaLkI_LgW9DYwQ"
w3 =Web3(Web3.HTTPProvider(rpc_url))
account =Account.create()

#create account eth
def create_account_and_save():
    privatekey = account.key.hex()
    public_key = account._key_obj.public_key.to_hex()
    address    = account.address

    #simpan hasi pembuatan akun
    filename =f"{address}.txt"
    with open(filename, 'w')as f:
        f.write(f"PrivateKey:{privatekey}\n")
        f.write(f"PublicKey:{public_key}\n")
        f.write(f"Address:{address}\n")
    print(f"{Fore.GREEN} Akun Baru berhasil dibuat dan disimpan di {filename}")

#check balance
def check_balance():
    address= input(f"{Fore.YELLOW} masukan address yang ingin di cek : ").strip()

    if not w3.is_connected():
        print(f"{Fore.RED} gagal terhubung RPC")
        return
    
    try:
        balance_wei = w3.eth.get_balance(address)
        balance_eth = w3.from_wei(balance_wei, 'ether')
        print(f"{Fore.CYAN} balance address {address} adalah : {balance_eth} ETH")
    except Exception as e:
        print(f"{Fore.RED} gagal cek saldo {e}")


def main():
    while True:
        print(f"{Fore.BLUE}\n============MENU============")
        print(f"{Fore.GREEN}1. Create Account And Simpan ke Txt")
        print(f"{Fore.GREEN}2. Cek Balance")
        print(f"{Fore.GREEN}0. Exit")

        pilihan = input(f"{Fore.WHITE} Pilih menu (1/2/3): ").strip()
        if pilihan =='1':
            create_account_and_save()
        elif pilihan =='2':
            check_balance()
        elif pilihan == '0':
            print(f"{Fore.YELLOW}Keluar Dari Program...")
            break
        else:
            print(f"{Fore.RED} pilihan tidak valid coba lagi!!...")
if __name__ == "__main__":
    main()



