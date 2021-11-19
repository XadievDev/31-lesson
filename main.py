#XadievDev
#31-lesson.Inkapsulyatsiya

#------------------------------------------------------------------------#

from uuid import uuid4

class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
    
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id

    def add_km(self,km):
        if km>=0:
            self.__km += km
        else:
            print("km ni kamaytirib bo'lmaydi.")
    
avto1 = Avto('GM','Malibu','qora',2021,40000,100)

#------------------------------------------------------------------------#

#Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
#Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
#Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing

class Talaba:
    __talabalar_soni = 0
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        Talaba.__talabalar_soni += 1
    
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni

talaba1 = Talaba('Amirbek','Xadiev',2006)

class Shaxs:
    __odamlar_soni = 0
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__id = uuid4()
        Shaxs.__odamlar_soni += 1
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

    @classmethod
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni
    
    def get_id(self):
        return self.__id
    
shaxs1 = Shaxs('Amirbek','Xadiev','FBB000001',2006)

