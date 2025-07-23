
import csv
class car:
 def __init__(s,b,m,p):
  s.b=b
  s.m=m
  s.p=float(p)
 def c(o):
  print(f"{o.b} {o.m} -- {o.p} Rs")
showroom =[]
print("Welcome to my mini showroom\n(type 'stop' to leave)")
print("——" * 60)
while True:
 b = input("Enter car brand name = ").strip()
 if b.lower() == "stop":
  break
 m = input("Enter car model name = ").strip()
 if m.lower() == "stop":
  break
 p = input("Enter car price = ").strip()
 if p.lower() == "stop":
  break
 if not p.replace(".","",1).isdigit():
  print("Enter only valid price???????????????")
  continue
 c = car(b,m,p)
 showroom.append(c)
 print("")
 print("--" * 25 ,"car detail added","--" * 25)
 print("——" * 60)
sb = input("\nEnter brand name for search car or (press enter key to skip)-->").strip()
if sb:
 print("**" * 60)
 print(f"\ncar from brand {sb}\n")
 f = False
 for ca in showroom:
  if ca.b.lower() == sb.lower():
   ca.c()
   f = True
  if not f:
   print("we don't have your car option[o_o]")
print("——" * 60)
sc = input("sort car by price? (yes/no) = ").strip().lower()
if sc == "yes":
 showroom.sort(key=lambda a: a.p)
 print("\ncar price sorted by low to high\n")
 for r in showroom:
  r.c()
tv = sum(car.p for car in showroom)
print("——" * 60)
print(f"total vale of car in showroom = {tv:.3f}")
print("——" * 60)
print("  " * 25 ,"FINAL INVENTORY","  " * 25)
for i,m in enumerate(showroom,1):
 print(f"{i}.",end=" ")
 m.c()
print(" " * 40 ,"THANKS YOU FOR VISITING OUR SHOWROOM"," " * 25)