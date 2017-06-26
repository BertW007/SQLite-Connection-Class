# SQLite-Connection-Class
A class to simplify sqlite operations with python. This project is not a professional project. The class I created to use in the project.

## Kullanım
SQLiteConnection/config.py içerisinde bulunan 
```
SQLiteHost = "test.db"
```
stringine sqlite databasemizin dizinini ekliyoruz. Artık classdan nesne türetilirken burada bulunan database bir connection oluşturulacaktır.

### Modülü Dahil Etmek
Connection kullanılırken dahil edilecek dosyanın en üst kısmına
```
from SQLiteConnection.database import SqlClass
```
eklememiz gerekir.

### Tüm Kayıtları Çekmek
Örneklerde kullanmak için bir nesne türetelim.
```
myClass = SqlClass()
```
Türettiğimiz bu class ile tüm kayıtları çekmek için
```
getAll = myClass.Get("SELECT * FROM example")
```
Burada dikkat etmemiz gereken Get() fonksiyonu tablodaki tüm kayıtları değil sql sorgusundan dönen tüm kayıtları bize getirecektir.
Dönen bu kayıtları şu şekilde kullanabiliriz.
```
for row in getAll:
    print(row["ID"],". Row:",row["Name"])
```

### İlk Satırı Çekmek
Sql sorgusundan dönen ilk satırı kullanmak istiyorsak şu şekilde kullanabilir.
```
getRow = myClass.GetRow("SELECT * FROM example WHERE ID = ?", ('1'))
```
Dönen kaydı kullanmak için ise şu yapı kullanabilir.
```
print(getRow["ID"],"Row Mail:",getRow["Mail"])
```
Eğer şöyle bir sorgu çalıştırsaydık
```
getRow = myClass.GetRow("SELECT * FROM example")
```
dönen tüm kayıtlar içerisinde en üstte olan kaydı dönderecekti.

### İlk Satırın İlk Sütunundaki Veriyi Almak
Sql sorgumuzda tek sütunluk bir veri çekiyorsak(Count gibi) bu fonksiyonu kullanabiliriz.
```
getOne = myClass.GetOne("SELECT Count(*) FROM example")
```
Şu şekilde kullanılabilir.
```
print("Count Row:",getOne)
```

### Kayıt Ekleme Ve Eklenen Kaydın ID'sini Döndürme
Sql tablomuza bir veri eklemek istiyorsak Insert() fonksiyonunu kullanabiliriz. Bu fonksiyon aynı zamanda eklenen kaydınız ID'sinide döndürür.
```
insert = myClass.Insert("INSERT INTO example(Name,Mail,Password) VALUES (?,?,?)", ('Denziel Washington','denzelwashington@gmail.com','denzel'))
print("Last Insert ID:",insert)
```

### Delete Ve Update Sorguları Ve Etkilenen Satır Sayısı
Sql tablomuzdan kayıt silme veye kaydı güncelleme için Exec() fonksiyonu kullanılabilir. Aynı zamanda etkilenen satır sayısını döndürür.
```
affectRow = myClass.Exec("UPDATE example SET Name = ? WHERE ID = ?",('Denzel Washington','1'))
print("Affected Row:",affectRow)
```
Uyarı: Select Sorgularında işe yaramamaktadır. -1 dönmektedir.