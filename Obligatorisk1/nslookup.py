import subprocess


blacklist_chars = ["<", ">", ";", " "]
whitelist_domains = (".dk", ".com")
read = input("Enter domain: ")

for i in blacklist_chars:
    if i in read:
        quit()
    else:
        if read.endswith(whitelist_domains):
            command = "nslookup {}".format(read)
            response = subprocess.check_output(command, shell=True, encoding="UTF-8")
            print(response)
            print("Succes")           
    break