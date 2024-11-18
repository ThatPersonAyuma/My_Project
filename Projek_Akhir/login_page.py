import pandas as pd
import time as tm
import numpy as np
import stdiomask as sm

DATE=np.datetime64("today")
DATE_LONG=len(np.datetime_as_string(DATE))
print(DATE)
#CONSTANT DATA, HANDLING IT CAREFULLY
DF=pd.read_csv("algo_dan_pemograman1\\Projek_Akhir\\data_user.csv")
DF.set_index("Username", inplace=True, drop=False)
DFSELLERDATA=pd.read_csv("algo_dan_pemograman1\\Projek_Akhir\\data_seller.csv").set_index("Username", drop=True)
USERNAME=DF["Username"]
USER='0' #Have not log in, '1' for customer, '2' for farmer (seller), and '3' for admin/developer
STATE='0' #State 0 for un-log in user and State 1 for log in person
DFCustomer=DF.loc[DF["Tipe User"]=="Customer"]
DFSeller=DF.loc[DF["Tipe User"]=="Seller"]
DFADMIN=DF.loc[DF["Tipe User"]=="ADMIN"]
#print(DF.loc["Ayuma"].values)
#print(DF.loc[DF["Tipe User"]=="Seller"])

def writeLog(username: str, user_type: str):
    """Write the login time of the user, using Indonesia WIB time"""
    time_wib=np.datetime64("now")+np.timedelta64(7, 'h')
    with open("algo_dan_pemograman1\\Projek_Akhir\\log_history.csv", mode="a") as f :
        f.write(f"{username},{user_type},{time_wib}\n")
    print("log has been written")
    #return time_wib

def getUserData(mode: str)-> list:
    """Get all of the user data
    
    return [Full Name, Address, E-Mail, Username/Name Of Bussiness, Password]"""
    user_fullName=getFullName()
    user_address=input("Alamat\t\t: ")
    user_email=getEMail()
    user_username=input(f"{mode}\t: ")
    user_password=sm.getpass("Password\t: ")
    return [user_fullName, user_address, user_email, user_username, user_password]

def signUp(user_type: str, mode: str, isSeller: bool=False)-> None:
    """Get the full data of user"""
    data=getUserData(mode)
    if isSeller:
        sellerData=getSellerData()
        with open("algo_dan_pemograman1\\Projek_Akhir\\data_seller.csv", "a") as f:
            f.write(f'{data[3]},"{sellerData[0]}","{sellerData[1]}","{sellerData[1]}"\n')
    #print(f"Nama Lengkap\t: {data[0]}\nAlamat\t\t: {data[1]}\nE-Mail\t\t: {data[2]}\n{mode}\t: {data[3]}\nPassword\t: {data[4]}")
    #df=pd.DataFrame([[user_fullName, user_address, user_email, user_username, user_password]], columns=["Nama Lengkap", "Alamat", "E-Mail", "Username", "Password"],)
    with open("algo_dan_pemograman1\\Projek_Akhir\\data_user.csv", 'a') as f:
       f.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{user_type}\n")

def getSellerData():
    """Used to get the product data of seller, combine it with getUserData Function. Set available product, requested/hold product (zero), and sold product (zero).
    
    return [available stock, hold stock]"""
    placeHolderAvailable={}
    placeHolderHS={}
    while(1):
        inputName=input("Masukkan nama produk: ")
        inputQuantity=input("Jumlah yang tersedia: ")
        inputDateStart=input("Gunakan tanggal dengan format YYYY-MM-DD untuk menjawab 2 pertanyaan terakhir\nTanggal panen: ")
        inputDateEnd=input("Produk kadaluarsa pada: ")
        #using update be careful
        placeHolderAvailable.update({inputName:{"Jumlah":inputQuantity,"Tanggal":[inputDateStart,inputDateEnd]}})
        placeHolderHS.update({inputName:0})
        while(1):
            choice=input("Apakah anda ingin memasukkan data lagi ('Y' untuk lanjut dan 'T' untuk berhenti)? ")
            match choice:
                case 'Y':
                    break
                case 'T':
                    return [placeHolderAvailable,placeHolderHS]
                case _:
                    pass

def signIn(df, val: str)-> str:
    i=0
    while(i<3):
        user_username=input("\nUsername\t: ")
        user_password=sm.getpass("Password\t: ")
        try:
            if checkData(df, user_username, [user_username, user_password]):
                print("\nYou are log in")
                tm.sleep(3)
                return [val, user_username]
            else:
                print("Wrong password, try again")
        except:
            print("Akun tidak ada, silakan periksa akun tiba")
        i=-~i
    print("Anda salah tiga kali.")
    for i in range(1,11):
        tm.sleep(1)
        print(f"Tunggu {10-i} detik lagi")
    return signIn(df, val)

def signInCostumer():
    global USER
    data=signIn(DFCustomer, '1')
    USER=data[0]
    writeLog(data[1], 'Costumer')
    customerHomePage(data[1])

def signInSeller():
    global USER
    USER=signIn(DFSeller, '2')[0]
    print("\nYou are a seller")

def signInAdmin():
    global USER
    USER=signIn(DFADMIN, '3')[0]
    print("\nYou are a admin")

def getFullName()-> str:
    """Get the full name of the user"""
    while(1):
        user_input=input("Nama Lengkap\t: ")
        user_input="".join(user_input.split("'"))
        print(user_input, user_input.title())
        if user_input==user_input.title() and "".join(user_input.split(" ")).isalpha() and "  " not in user_input:
            return user_input
        else:
            print("Inputan nama harus huruf besar pada setiap kata.\nKarakter unik yng diperbolehkan hanya \"'\" dan setiap kata dipisahkan oleh satu spasi 🤓")

def getEMail()-> str:
    """Get email address by checking if \"@gmail.com\" is in the string"""
    pre_email=input("E-Mail\t\t: ")
    if "@gmail.com" in pre_email:
        return pre_email
    else:
        return getEMail()

def checkData(data: pd.DataFrame, username: str, value: list|dict)-> bool:
    """Check if the value is in data (DataFrame). Return True if it is in data (DataFrame), otherwise False."""
    if username in data.index:
        for i in value:
            if i in data.loc[username].values:
                pass
            else:
                return False
        return True
    else:
        print("Error")
        raise KeyError

def deleteData(username: str)-> None:
    global DF
    """To delete a data."""
    DF.drop(index=username, inplace=True)
    DF.to_csv("algo_dan_pemograman1\\Projek_Akhir\\data_user.csv", mode="w", index=False)

def signInChoice(sign_in: bool=True):
    while(1):
        user_type=input("Masukkan inputan sesuai nomor di atas: ")
        if user_type == '1':
            return signInCostumer() if sign_in else signUp('Customer')
        elif user_type == '2':
            return signInSeller() if sign_in else signUp('Seller')
        elif user_type == '3' and sign_in:
            return signInAdmin()
        print(USER)

def signInPage():
    print("-"*(61))
    print("|"+f"{"Silakan Masukkan Inputan angka Sesuai Keterangan di Bawah".center(59)}|")
    print('|'.ljust(6)+"1. Pelanggan".ljust(54)+'|')
    print('|'.ljust(6)+"2. Penjual".ljust(54)+'|')
    print('|'.ljust(6)+"3. Admin".ljust(54)+'|')
    print("-"*(61))
    signInChoice()

def signUpPage():
    print("-"*(61))
    print("|"+f"{"Silakan Masukkan Inputan angka Sesuai Keterangan di Bawah".center(59)}|")
    print('|'.ljust(6)+"1. Pelanggan".ljust(54)+'|')
    print('|'.ljust(6)+"2. Penjual".ljust(54)+'|')
    print('|'.ljust(6)+"0. Exit".ljust(54)+'|')
    print("-"*(61))
    signInChoice(sign_in=False)

def customerHomePage(name: str):
    print("-"*(61))
    print("|"+f" O {name}".ljust(58-DATE_LONG)+f"{DATE} "+"|\n|"+f"{"Silakan Masukkan Inputan angka Sesuai Keterangan di Bawah".center(59)}|")
    print("|"+("-"*59)+"|")
    print('|'.ljust(6)+"1. Belanja".ljust(54)+'|')
    print('|'.ljust(6)+"2. Keranjang".ljust(54)+'|')
    print('|'.ljust(6)+"0. Exit".ljust(54)+'|')
    print("-"*(61))
    homePageChoice(name)

def homePageChoice(name: str):
    while(1):
        user_type=input("Masukkan inputan sesuai nomor di atas: ")
        if user_type == '1':
            return shoppingPage(name)
        elif user_type == '2':
            return signInSeller()
        elif user_type == '3':
            return signInAdmin()
        print(USER)

def shoppingPage(name: str):
    print("-"*(61))
    print("|"+f" O {name}".ljust(58-DATE_LONG)+f"{DATE} |")
    place_holder={}
    order=1
    namaPenjual=DFSELLERDATA.index
    for i in namaPenjual:
        data=printItemSeller(i, order)
        order=data[0]
        place_holder.update(data[1])
    print("-"*(61))
    print(place_holder)
    while(1):
        try:
            choice=int(input("Pilih nomor product: "))
            if choice>0:
                dataProduct=place_holder[choice]
                orderProduct(name, dataProduct, namaPenjual, choice)
            elif choice==0:
                pass
            break
        except:
            print("\nInputan harus berupa angka saja.")

def orderProduct(name: str, dataProduct: list, namaPenjual: pd.Index, choice: int):
    dataTersedia=eval(DFSELLERDATA.iloc[dataProduct[0], 0])
    print()
    print("-"*(61))
    print("|"+f" O {name}".ljust(58-DATE_LONG)+f"{DATE} |")
    printASeller(username=namaPenjual[dataProduct[0]], order=choice, data=dataTersedia, i=dataProduct[1], num=dataProduct[0])
    print("-"*(61))
    dataDipesan=eval(DFSELLERDATA.iloc[dataProduct[0], 1])
    bawah=1
    atas=dataTersedia[dataProduct[1]]["Jumlah"]
    #if name in dataDipesan:
    #    if choice==dataDipesan
    while(1):
        try:
            quantityProduct=int(input(f"Berapa banyak {dataProduct[1]} yang ingin anda beli? "))
            if bawah<=quantityProduct<=atas:
                date=f"{np.datetime64("now", "s")+np.timedelta64(7, "h")}"
                dataDipesan[dataProduct[1]].update({name: [quantityProduct,date]})
                break
            else:
                print(f"\nInputan haruslah antara {bawah} sampai {atas}.")
        except:
            print("\nInputan harus berupa angka saja.")
    DFSELLERDATA.iloc[dataProduct[0], 1]=f"{dataDipesan}"
    dataTersedia[dataProduct[1]].update({"Jumlah": dataTersedia[dataProduct[1]]["Jumlah"]-quantityProduct})
    DFSELLERDATA.iloc[dataProduct[0], 0]=f"{dataTersedia}"
    DFSELLERDATA.to_csv("algo_dan_pemograman1\\Projek_Akhir\\data_seller.csv")
    print(DFSELLERDATA)   

def printItemSeller(username: str, order: int=1):
    for index, x in enumerate(DFSELLERDATA.index):
        if x==username:
            num=index
    data=eval(DFSELLERDATA.iloc[num, 0])
    place_holder={}
    for i in data:
        printASeller(username=username, order=order, data=data, i=i, num=num)
        place_holder.update({order: [num, i]})
        order+=1
    return [order, place_holder]

def printASeller(username: str, order: int, data: dict, i:str, num: int):
    print("|"+("-"*59)+"|")
    print("|"+f" {order}".ljust(4)+f"| {username}".ljust(29)+f"Tanggal Panen: {data[i]["Tanggal"][0]} "+"|")
    print("|"+f"----- {i} | Stock: {data[i]["Jumlah"]} ".ljust(45)+f"Rate: {DFSELLERDATA.iloc[num, 3]} ".rjust(14)+"|")

def searchProduct(name: str):
    product=input("Masukkan nama buah/sayur: ")
    list_nama=DFSELLERDATA.index
    order=1
    print("-"*61)
    print("|"+f" O {name}".ljust(58-DATE_LONG)+f"{DATE} |")
    for index, i in enumerate(DFSELLERDATA["Tersedia"]):
        if product in i:
            i=eval(i)
            print("|"+("-"*59)+"|")
            print("|"+f" {order}".ljust(4)+f"| {list_nama[index]}".ljust(29)+f"Tanggal Panen: {i[product]["Tanggal"][0]} "+"|")
            print("|"+f"----- {product} | Stock: {i[product]["Jumlah"]} ".ljust(45)+f"Rate: {DFSELLERDATA.iloc[index, 3]} ".rjust(14)+"|")
            order+=1
    print("-"*61)
    #print()
    #if product in DFSELLERDATA[DFSELLERDATA["Tersedia"]]

def firstPage():
    print("-"*(61))
    print("|"+"Selamat Datang".center(59)+"|\n|"+f"{"Silakan Masukkan Inputan angka Sesuai Keterangan di Bawah".center(59)}|")
    print('|'.ljust(6)+"1. Sign In".ljust(54)+'|')
    print('|'.ljust(6)+"2. Sign Up".ljust(54)+'|')
    print('|'.ljust(6)+"0. Exit".ljust(54)+'|')
    print("-"*(61))
    choice=input("Masukkan inputan sesuai nomor di atas: ")
    match choice:
        case '1':
            return signInPage()
        case '2':
            return signUpPage()

def main():
    firstPage()


def correctDataSeller(df: pd.DataFrame)->pd.DataFrame:
    #df=df.map(eval, )
    #print(df[["Tersedia", "Dipesan", "Terjual"]].values)
    #print()
    #print(df["Tersedia"])
    #return df
    pass
    
main()
#signUp('Customer', 'Nama Toko', isSeller=True)

#searchProduct("Tatang")
#shoppingPage("Bambang")
#print(DFSELLERDATA["Tersedia"])
#main()
#homePageChoice("Saya")
#DFSELLERDATA=correctDataSeller(DFSELLERDATA.set_index("Username", drop=False))
#order=printItemSeller("Bagus Maragus")
#printItemSeller("")
#print(DFSELLERDATA)
#print(DFSELLERDATA.iloc['Bagus Maragus'])
#df=pd.read_csv("algo_dan_pemograman1\\Projek_Akhir\\data_seller.csv")
#print(df)
#correctDataSeller(df)
# df.info()
#Accessing dictionary from data_seller using eval function
#print(eval(df.iloc[0,1]).keys())
#main()
#print(DF.index)
#print(DF)
#deleteData("ebdbdu")
#print(DF)
#print('Ayum' in DF["Username"])