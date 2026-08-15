with open("server.log","r") as file:
   for line in file:
      line=line.strip()
      print(line)

      info_count=0
      Warning_count=0
      error_count=0

      if "INFO"in line:
         info_count+=1
      elif "WARNING" in line:
         Warning_count+=1
      elif "ERROR" in line:
         error_count+=1

print("INFO",info_count)
print("WARNING",Warning_count)
print("ERROR",error_count)

 

      


