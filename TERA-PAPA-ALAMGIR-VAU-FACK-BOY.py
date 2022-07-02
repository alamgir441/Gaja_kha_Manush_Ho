import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
    os.system('git pull')
    import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations TERA PAPA ALAMGIR VAU FACK BOY! Your Device Support this Tools")
    print(' TERA PAPA ALAMGIR VAU FACK BOY 😍 ')
    os.system('xdg-open https://www.Facebook.com/Tera.Papa.Alamgir.441');time.sleep(3)
    from AKING64 import main
    main()
elif bit == '32bit':
    print("\x1b[1;92m Congratulations TERA PAPA ALAMGIR VAU FACK BOY! Your Device Support this Tools")
    print(' TERA PAPA ALAMGIR VAU FACK BOY 😍 ')
    os.system('xdg-open https://m.me/Tera.Papa.Alamgir.441');time.sleep(3)
    from AKING32 import main
    main()
