# AmazonWebScraping

Amazon Web Scraping projemde ağırlıklı olarak python dilini kullandım.Çoğunlukla Flask, Matplotlib ve Selenium kütüphanelerini kullandığım projemde Amazon sitesinden belirli bir linkteki ürünlerin Marka, Fiyat ve Ürün ismi verilerini çekip güncel bir şekilde görselleştirilerek bir Flask sitesine eklenmesini sağlıyor.

Selenium klasörünün içindeki main.py kodu Amazon'dan belirli bir linki açıyor ve sayfada bulunan ürünlerin isimlerini ve fiyatlarını alıyor.Daha sonra ileri sayfaya geçiyor ve bu işlemi sayfalar bitene kadar tekrarlıyor.Daha sonra alınan Marka, Ürün ismi ve Fiyat verilerini eşzamanlı olarak bir csv dosyasına kaydediyor ve bu csv dosyasını flask kodunda kullanılmak üzere ismi AmazonVeri.json olan bir json dosyasına dönüştürüyor.

Flask klasöründeki app.py ise kaydedilen AmazonVeri.json dosyasındaki verileri Matplotlib kütüphanesi ile 'Markaların Ortalama Fiyatları' grafiğine dönüştürüyor ve bir Flask sitesi açarak bu grafiği Flask sitesine ekliyor.

Flask klasöründeki main.py ise Subprocess kütüphanesi ile önce Selenium klasöründeki main.py'ın çalışmasını sağlayarak AmazonVeri.json dosyasındaki verileri güncellememizi sağlıyor, ardından Flask klasöründeki app.py'ı çalıştırarak bu verilerin grafiğe dökülmesini ve flask sitesi açarak grafiğin Flask sitesine eklenmesini sağlıyor.
