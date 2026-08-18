write_your_name = input("write your name")
audits_done = int(input("no of audits"))
certificates_issued = int(input("certificates"))
success_rate = (certificates_issued/audits_done)*100
print("Name : " + write_your_name)
print("No. of audits done : " + str(audits_done))
print("No. of Certificates issues : " + str(certificates_issued))
print("Success Rate : " + str(success_rate))