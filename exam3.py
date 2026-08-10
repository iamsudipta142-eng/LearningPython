enter_nc = int(input("number of nc"))
if enter_nc == 0:
    print("Certificate to be granted")
    print("technical reviewer passed this")
elif enter_nc <= 5:
    print("One more time nc to be checked")
elif enter_nc <= 10:
    print("Major NC")
elif enter_nc <= 30:
    print("Re audit to be done")
else:
    print("decision to be taken by certification body")
