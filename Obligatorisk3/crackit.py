from passlib.hash import sha512_crypt
password = "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0"

for i in range(0, 10):
    index0 = i
    for p in range(0, 10):
        index1 = p
        for k in range(0, 10):
            index2 = k
            res = str(index0)+str(index1)+str(index2)
            hash = sha512_crypt.using(salt = "penguins", rounds=5000).hash(res)
            if (hash == password):
                print("Password: ", res)
                break


