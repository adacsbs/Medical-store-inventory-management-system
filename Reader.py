from Scanner import *

#image_path=input("Enter Image path: ")
image_path="Images\Test5.png"
main_list=[]
main_list=scan_image(image_path).split()
print(main_list)
#print("Price: ",main_list[6])

