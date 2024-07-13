import mysql.connector
from datetime import datetime 
from connection import connection

class Student():
    connection = connection
    mycursor = connection.cursor()
    
    def __init__(self,studentNumber,name,surname,birthdate,gender):
        self.ogrenci_no = studentNumber
        self.isim = name
        self.soyisim = surname
        self.dogum_yili = birthdate
        self.cinsiyet = gender

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata: ", err)
        finally:
            Student.connection.close()
            print("Database bağlantısı kapandı.")

ogrenciler=[
    ("901","Mehmet","Bozoğlu",datetime(2005, 5, 17),"E"),
    ("902","Serpil","Uçar",datetime(2005, 6, 17),"K"),
    ("903","Ece","Öncül",datetime(2005, 7, 7),"K"),
    ("904","Sema","Asan",datetime(2005, 9, 23),"K"),
    ("905","Ömer","Çay",datetime(2004, 7, 27),"E"),
    ("906","Diyar","Aktaş",datetime(2003, 8, 25),"E")
]

Student.saveStudents(ogrenciler)