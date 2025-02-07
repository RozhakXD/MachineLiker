try:
    import requests, time, os
    from rich import print as Println
    from rich.panel import Panel
    from requests.exceptions import RequestException
    from rich.console import Console
except (ModuleNotFoundError, ImportError):
    print("[Error] Please install the required modules!")
    exit()

FACEBOOK, MACHINE_LIKER = {
    "Cookies": None,
}, {"Cookies": None, "UserID": None}

def Login(cookies_facebook: str) -> str:
    with requests.Session() as session:
        session.headers.update(
            {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "X-Requested-With": "com.machinelikers.app",
                "Accept-Encoding": "gzip, deflate",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Connection": "keep-alive",
                "Host": "machine-likers.com",
                "Sec-Fetch-Dest": "document",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A908N Build/PQ3A.190605.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 V19"
            }
        )
        response = session.get("https://machine-likers.com/appindexnew.php")
        cookies_string = "; ".join([str(x) + "=" + str(y) for x, y in session.cookies.get_dict().items()])
        session.headers.update(
            {
                "Cookie": "{}".format(cookies_string)
            }
        )
        response2 = session.get("https://machine-likers.com/aplogin.php?cookie={}".format(str(cookies_facebook).replace(" ", "%20")))
        if 'user_id' in session.cookies.get_dict():
            cookies_string = "; ".join([str(x) + "=" + str(y) for x, y in session.cookies.get_dict().items()])
            session.headers.update(
                {
                    "Cookie": "{}".format(cookies_string),
                    "Sec-Fetch-Site": "same-origin"
                }
            )
            response = session.get("https://machine-likers.com/aphome.php")
            if 'Switch Account' in response.text:
                Println("[bold bright_black]   ──> [bold green]LOGIN SUCCESSFUL!        ", end="\r")
                time.sleep(2.5)
                user_id = session.cookies.get_dict()['user_id']
                MACHINE_LIKER.update(
                    {
                        "Cookies": cookies_string,
                        "UserID": user_id
                    }
                )
                return "Login Success!"
            else:
                Println("[bold bright_black]   ──> [bold red]LOGIN FAILED!        ", end="\r")
                time.sleep(2.5)
                return "Login Failed!"
        else:
            Println("[bold bright_black]   ──> [bold yellow]LOGIN FAILED!        ", end="\r")
            time.sleep(2.5)
            return "Login Failed!"

def SendLike(post_links: str) -> str:
    with requests.Session() as session:
        data = {
            "token": f"{MACHINE_LIKER['UserID']}",
            "id": f"{post_links}",
            "type[]": [1],
            "cf-turnstile-response": None # This is a response from cloudflare!
        }
        session.headers.update(
            {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "Cache-Control": "max-age=0",
                "Connection": "keep-alive",
                "Content-Length": "{}".format(len(data)),
                "Content-Type": "application/x-www-form-urlencoded",
                "Cookie": "{}".format(MACHINE_LIKER['Cookies']),
                "Host": "machine-likers.com",
                "Origin": "https://machine-likers.com",
                "Referer": "https://machine-likers.com/apautoreact.php",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A908N Build/PQ3A.190605.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Safari/537.36 V19",
                "X-Requested-With": "com.machinelikers.app"
            }
        )
        response = session.post("https://machine-likers.com/apautoreact.php", data=data)
        session.headers.pop("Content-Length")
        session.headers.pop("Content-Type")
        response5 = session.get("https://machine-likers.com/apsbs.php")
        if 'Your order Place successfully.' in response5.text:
            return "Submit Success!"
        else:
            return "Submit Failed!"

def Banner() -> None:
    os.system('cls' if os.name=='nt' else 'clear')
    Println(Panel(r"""[bold red]●[bold yellow] ●[bold green] ●[/]
[bold red]   __  ___         __   _          __   _ __          
  /  |/  /__ _____/ /  (_)__  ___ / /  (_) /_____ ____
 / /|_/ / _ `/ __/ _ \/ / _ \/ -_) /__/ /  '_/ -_) __/
[bold white]/_/  /_/\_,_/\__/_//_/_/_//_/\__/____/_/_/\_\\__/_/  
 
       [underline red]Free Facebook Likes - Coded by Rozhak-XD""", width=58, style="bold bright_black"))
    return None

def Feature() -> None:
    Banner()
    Println(Panel(f"[bold white]Silakan Masukkan Cookies Akun Facebook, Anda Harus Menggunakan Akun Palsu / Akun Baru Untuk Login!", width=58, style="bold bright_black", title="[bold bright_black]>> [Login Cookies] <<", subtitle="[bold bright_black]╭──────", subtitle_align="left"))
    cookies_facebook = Console().input("[bold bright_black]   ╰─> ")
    if 'c_user' in cookies_facebook and 'xs' in cookies_facebook:
        Println(Panel(f"[bold white]Silakan Masukkan Tautan Postingan Yang Ingin Diberikan Like, Anda Bisa Mendapatkannya Melalui Browser!", width=58, style="bold bright_black", title="[bold bright_black]>> [Post Links] <<", subtitle="[bold bright_black]╭──────", subtitle_align="left"))
        post_links = Console().input("[bold bright_black]   ╰─> ")
        Println(Panel(f"[bold white]Anda Bisa Menggunakan[bold yellow] CTRL + C[bold white] Jika Stuck Dan Gunakan[bold red] CTRL + Z[bold white] Jika Ingin Berhenti!", width=58, style="bold bright_black", title="[bold bright_black]>> [Notes] <<"))
        status_login = Login(cookies_facebook)
        if status_login == "Login Success!":
            Looping = 0
            while Looping <= 10:
                try:
                    status_likes = SendLike(post_links)
                    if status_likes == "Submit Success!":
                        Println(Panel(f"""[bold white]Status: [bold green]Successfully!
[bold white]Link: [bold red]{post_links}
[bold white]Likes: [bold green]+50""", width=58, style="bold bright_black", title="[bold bright_black]>> [Success] <<"))
                        for i in range(1800, 0, -1):
                            Println(f"[bold bright_black]   ──> [bold white]RESTARTING IN {i} SECONDS!     ", end="\r")
                            time.sleep(1)
                        Looping += 1
                    else:
                        Println("[bold bright_black]   ──> [bold red]LIKES FAILED!        ", end="\r")
                        Login(cookies_facebook)
                        continue
                except RequestException:
                    Println("[bold bright_black]   ──> [bold red]CONNECTION ERROR!        ", end="\r")
                    time.sleep(10.0)
                    continue
                except KeyboardInterrupt:
                    Println("                                                    ", end="\r")
                    time.sleep(2.5)
                    continue
            Println(Panel(f"[bold green]Selamat![bold white] Anda Telah Mencapai Batas Harian Pengiriman Like, Kembalilah Esok Hari!", width=58, style="bold bright_black", title="[bold bright_black]>> [Completed] <<"))
            exit()
        else:
            Println(Panel(f"[bold red]Maaf, Cookies Facebook Yang Anda Masukkan Sudah Tidak Valid, Silakan Coba Lagi!", width=58, style="bold bright_black", title="[bold bright_black]>> [Login Failure] <<"))
            exit()
    else:
        Println(Panel(f"[bold red]Maaf, Cookies Facebook Yang Anda Masukkan Salah, Silak\nan Coba Lagi!", width=58, style="bold bright_black", title="[bold bright_black]>> [Cookies Wrong] <<"))
        exit()

if __name__ == '__main__':
    try:
        os.system('git pull')
        Feature()
    except Exception as e:
        Println(Panel(f"[bold red]{str(e).title()}!", width=58, style="bold bright_black", title="[bold bright_black]>> [Error] <<"))
        exit()
    except KeyboardInterrupt:
        exit()