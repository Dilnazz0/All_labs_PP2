import os
p=input("enter a path to insert files:")
for i in range(65,91):
    with open(os.path.join(p,chr(i)+".txt"),"w")as f:
        f.write(f"This is file {chr(i)}")
    print(f"{chr(i)}.txt created successfully")