## Morse challenge 📻

### Objectives 🎯

Bu challenge’ta şunları öğreneceğiz:
-Büyük problemleri parçalara ayırarak küçük problemler hâlinde çözmek.
-Farklı module’ler oluşturmak ve başka bir module içindeki function’ları kullanmak.
-Testleri verimli bir şekilde çalıştırmak.(**run tests efficiently**)
-**Encoding ve decoding** kavramlarına aşina olmak: Bunu Deep Learning module’ünde tekrar göreceğiz.


### ❔ Arka plan

Wikipedia’ya göre 1836’dan itibaren Amerikalı sanatçı Samuel F. B. Morse, Amerikalı fizikçi Joseph Henry ve Alfred Vail bir elektrikli telgraf sistemi geliştirdiler. Bu sistem, telgraf sisteminin alıcı ucunda bulunan bir elektromıknatısı kontrol eden elektrik akımı darbelerini kablolar üzerinden iletiyordu. Sadece bu darbeler ve aralarındaki sessizliği kullanarak doğal dili iletebilmek için bir kod gerekiyordu. Yaklaşık 1837 civarında Morse, modern International Morse code’un erken bir öncülünü geliştirdi.

Bu alıştırmada bir Morse code encoder ve decoder yazacağız. Yalnızca İngiliz alfabesindeki 26 harfi (“A” -> “Z”) ele alacağız ve diğer tüm karakterleri (sayılar, noktalama işaretleri vb.) yok sayacağız.

### ⚙️ Kurulum

Bu challenge için, klasörün kök dizininden çalıştığından emin ol ve VS Code’u da oradan aç:

```bash
cd ~/code/<user.github_nickname>/{{ local_path_to("01-Python/01-Programming-Basics/06-Morse-Code") }}
code .
```

Bu challenge’ta birden fazla dosya ile çalışacağız, bu yüzden her zaman bu konumdan çalışman önemli.

### 🏗️ Workflow

Yazdığımız kodu, tekrar kullanılabilir birden fazla küçük module’e böleceğiz. Sonra bunları import etmemiz gerekecek. Önce `morse` klasöründeki dosyalara bakarak başla. `mapping.py` dosyasında, alfabenin harfleri için Morse code içeren bir dictionary’yi sana zaten verdik.

### ➡️ Encoder’ı yaz

Önce, morse/encoder.py içinde encode method’unu implement et. Bu method parametre olarak bir text alacak ve bunun Morse karşılığını döndürecek. Aynı kelime içindeki harfler arada bir boşluk olacak şekilde, kelimeler ise | karakteri ile ayrılacak.

Örneğin "Hi Guys" cümlesi ".... ..|--. ..- -.-- ..." şeklinde encode edilmelidir.

Karmaşıklığı azaltmak için iki function yazarak ilerle: önce tek bir kelimeyi encode eden bir function yaz. Sonra bir cümleyi encode etmek için encode function’ı içinde encode_word function’ını çağırabilirsin.

### 🧪 Kodunu çalıştırma ve test etme

Testleri çalıştırmadan önce kodunun hatasız çalıştığından emin ol. Deneme yapabilmen için if __name__ == "__main__" bloğunu ekledik. Bu challenge’ta birden fazla dosya kullandığımız için kodumuzu biraz farklı şekilde çalıştıracağız.

Kodunu çalıştırmak için şunu yaz:

```bash
python -m morse.encoder
```

Bu, `morse` package’i içindeki `encoder` module’ünü çalıştırır. Bizim durumumuzda module, `encoder.py` dosyasıdır, package ise module’lerin bir koleksiyonudur.
Burada dikkat et: import ederken kullandığımız yapının aynısını kullanıyoruz; ayırmak için `.`  kullanıyoruz ve sonuna `.py` eklemiyoruz.

<details>
  <summary markdown='span'>
  ⛓️‍💥 Getting an error <code>No module named 'morse'</code>?
  </summary>

Terminalin muhtemelen challenge’ın kök klasöründe değil. Belki `morse`  klasörüne geçtin? Öyleyse terminalde bir seviye yukarı çık.

Ya da VS Code’u `morse`  klasörünün içinden mi açtın? Bu durumda VS Code’u kapat ve bu challenge’ın ana klasöründen tekrar aç.

Birden fazla dosya kullandığında, kodu nereden çalıştırdığın önem kazanır. Bu dersler ilerledikçe bu işi daha az zahmetli hâle getiren yöntemler göreceğiz.



</details>

<details>
  <summary markdown='span'>
  🤔 Neden bu yöntemi kullanıyoruz? [Advanced remark - Optional]
  </summary>

Python, birden fazla dosya kullandığında biraz karışık hâle gelebiliyor.

 `python morse/encoder.py` komutunu çalıştırdığımızda Python, `.py` dosyasının konumunu, package ve module aradığı path’e ekler, yani `./morse/`. Ancak burada `morse` package’ini bulamaz sadece, `encoder` ve `mapping` module’lerini görür. Bu yüzden mapping’den import etmek için `from mapping import MORSE`yazmamız gerekir.

Sorun şu ki daha sonra testleri çalıştırdığımızda Python, arama path’ine `.py` dosyalarının konumunu değil, o anki çalışma konumumuzu ekler. Bu yüzden bu sefer de `from morse.mapping import MORSE` yazmamız gerekir.

`python -m morse.encoder` çalıştırdığımızda Python, arama path’ine mevcut konumumuzu ekler. Burada `morse` module’ünü bulabilir. Dolayısıyla `from morse.mapping import MORSE` yazabiliriz. Bu da testlerimizle birlikte sorunsuz çalışır. Problem çözülmüş olur.


</details>

Bu kısım çalıştıktan sonra encoder için testleri çalıştırabilirsin. make komutunu kullanabilirsin ama bu tüm testleri çalıştırır; henüz yazmadığımız decoder testlerini de. Bunun yerine şunu çalıştır:

```bash
pytest -v -k encoder
```

> **Neden -v ve -k kullanıyoruz?**
>
> -v ile pytest’e, bir test class’ı içindeki her bir testi ayrı ayrı raporlamasını söylüyoruz. Bir de -v olmadan dene, farkı gör.
>
> Sondaki -k encoder ile pytest’ten adında "encoder" geçen testleri çalıştırmasını istiyoruz.
>
> Bu tür koşulları birleştirebilirsin: pytest -v -k "encoder and not pipe"
Bu komut, adında "encoder" geçen ama "pipe" geçmeyen testleri çalıştırır.

Decoder’a geçmeden önce şunları yapmayı unutma:

```bash
git add morse/encoder.py
git commit -m "Finished the encoder"
git push
```

### ⬅️ Decoder’ı yaz

Encoder çalışır hâle geldikten sonra, tam tersini yapacak olan `decode` method’u üzerinde çalışmaya başlayabilirsin. Bu method `morse/decoder.py` içinde olacak!

Yine önce kodu çalıştır (`python -m morse.decoder`), sonra sadece decoder testlerini çalıştır.

Morse code’u elle yazmak zorunda kalmadan kodunu nasıl deneyebilirsin? `if __name__ == "__main__"` bloğunda önce encoder function’larını kullanarak text’i Morse code’a çevirebilirsin. Sonra **de**coder function’larını kullanarak tekrar text’e decode edersin. Sonuç, orijinal girdinle (uppercase hâlinde) aynı olmalıdır.

Son bölüme geçmeden önce değişikliklerini commit edip push etmeyi unutma!


### ✅ Tüm Testleri Çalıştırma

Encoder ve decoder işini bitirdiğinde, tüm testleri çalıştırma zamanı. Bu sefer direkt `make`çalıştırabilirsin.

Tüm testlerin yeşil geçmesi gerekiyor. Geriye kalan tek şey iyi bir coding style elde etmek. 10/10 aldığından emin ol. Eğer neden iyi bir style skoru alamadığını anlamıyorsan, bir TA’ye sor.

Bu kısmı da bitirdikten sonra tekrar commit ve push yap.

### 💡 Encoding ve decoding hakkında son bir söz

Burada uyguladığımız hâliyle encoding ve decoding, veriyi iletim veya depolama için belirli bir formata dönüştürme ve daha sonra orijinal bilgiyi geri elde etmek için bu işlemi tersine çevirme sürecidir.

Yani bir mesajı encode edip sonra decode edersen, teoride orijinal girdiyi geri alman gerekir, değil mi?

Ama gerçekten öyle mi oldu? Tam olarak değil: Morse code case-insensitive’dir. Yani a ve A aynı code’a encode edilir. Dolayısıyla decode ettiğimizde küçük/büyük harf bilgisi kaybolur; yani text’in başta büyük harfli mi yoksa küçük harfli mi olduğu bilgisini kaybetmiş oluruz.

Deep Learning’de de benzer şeylerin olduğunu göreceğiz. Takipte kal !