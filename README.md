# Proje_Odevim

- Bu projede Raspberry Pi 3 ile Bigisayar arasındaki haberleşmeyi sağlamak üzere tasarlanmıştır.
- Bu projede veri olarak karşı tarafa gönderilen zaman ve lokasyon bilgisidir. Bu sadece bir örnektir. İstediğiniz tipte, istediğiniz yapıda veri alışverişi TCP/IP ekosistemi ile yapılabilir.
- Burada iki tane cihaz kullanılmasına rağmen teorik olarak birden fazla cihazla da server/client yapısı bağlamında bir sistem oluşturulabilir.

- Server tarafı
  
  
  - "serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)" yapısı ile socket nesnesi oluşturulmuştur.
  - " host = '192.168.1.38' " Bu tanım ile rasperry ait olmak zorunda olan(client o çünkü) ip adresi tanumlanmıştır.
  - "port = 2613" Bu tanım ile yukarıda belirtilen ip adresine ait port numarası oluşturulmuştur. Bu port üzerinden haberleşme sağlanmıştır. Herhangi bir port numarası     belirlenebilir.
  - " serversocket.bind((host, port)) " yukarıda belirtilen bilgilere göre server soketi oluşturulmuştur.
  - Projede birden fazla değer almak için "while" döngüsü kullanılmıştır. "Try-Exception" yapısı ise olası bağlantı problemlerini ortadan kaldırmak için kullanılmıştır.
  - " g = geocoder.ip('me') " kendi ip numaramıza bağlı lokasyon bilgisini geocoder kütüphanesi vasıtası ile bu şekilde alınmıştır.
  -     string_1 = str(g.city)
        string_2 = str(datetime.datetime.now())  yapıları ile hem şehir bilgisini hemde o zamana ait olan gün ve saat bilgisini birer string değişkenine argüman olarak aktarılmıştır. 
  - " (clientsocket, address) = serversocket.accept() " bu satırda soket doğrulaması tamamlanmıştır ve veri gönderilmesi işlemine geçilecektir.
  - " data_total = string_1 + string_2 " iki string değişkeni de birleştirilmiştir.
  - " clientsocket.send(data_total.encode()) " client için yukarıdaki toplam string argümanı gönderilmiştir.
