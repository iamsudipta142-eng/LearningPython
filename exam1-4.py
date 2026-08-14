company_name = input("Company name")
director_name = input("director name")
location = input("location")
established_year = str(input("established year"))
services = ["IT Services",
            "MIS & DATABASE SYSTEM",
            "SAFETY AUDIT",
            "CONSUltancy"]
count = 1
print("Company Name : " + company_name)
print("Who is the director : " + director_name)
print("location : " + location)
print("Establsihed Year : " + established_year)
for service in services:
    print(str(count) + "." + (service))
    count = count +1 