for num in range(2,21):
    with open(f"table-{num}.txt","w") as f:
          
        for i in range(1,11):
            f.write(f"{num} x {i} = {num*i}\n")
            

        

                
