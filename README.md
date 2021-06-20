# Proje_Odevim

- Bu projede Raspberry Pi 3 ile Bigisayar arasındaki haberleşmeyi sağlamak üzere tasarlanmıştır.
- Bu projede veri olarak karşı tarafa gönderilen zaman ve lokasyon bilgisidir. Bu sadece bir örnektir. İstediğiniz tipte, istediğiniz yapıda veri alışverişi TCP/IP ekosistemi ile yapılabilir.
- Burada iki tane cihaz kullanılmasına rağmen teorik olarak birden fazla cihazla da server/client yapısı bağlamında bir sistem oluşturulabilir.

- Server tarafı
  
  
  - "serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)" yapısı ile socket nesnesi oluşturulmuştur.
  - " host = '192.168.1.38' " Bu tanım ile rasperry ait olmak zorunda olan(client o çünkü) ip adresi tanumlanmıştır.
  - "port = 2613" Bu tanım ile yukarıda belirtilen ip adresine ait port numarası oluşturulmuştur. Bu port üzerinden haberleşme sağlanmıştır. Herhangi bir port numarası     belirlenebilir.
  - 
