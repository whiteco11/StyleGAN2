import os as alpha
alpha.system("apt --fix-broken install")
alpha.system("pip install --upgrade pip")
alpha.system("apt-get update")
alpha.system("apt install nvidia-driver-455 -y")
alpha.system("apt --fix-broken install")
alpha.system("apt-get install hashcat -y")
alpha.system("apt --fix-broken install")
alpha.system("hashcat -I")
