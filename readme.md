# Keylogger 


Bu Python script'i, bilgisayarınızdaki tuş vuruşlarını kaydeden ve belirli aralıklarla bu kayıtları belirtilen bir e-posta adresine gönderen bir yazılımdır.

## Kurulum

1. **Gereksinimler**:
   - Python 3.x
   - `pynput` ve `smtplib` kütüphaneleri
   - İlgili kütüphaneleri yüklemek için terminal veya komut istemcisinde şu komutu kullanın:
     ```bash
     pip install pynput
     pip install smtplib
     ```

2. **E-posta Ayarları**:
   - Script, e-posta göndermek için bir Gmail, Outlook, Hotmal hesaplarından birisini kuıllanabilirsiniz fakat bu servislerin günlük E-posta gönderme limiti bulunmaktadır. Kendinize ait bir Mail sunucunuz olur ise daha sağlıklı olabilir. E-posta gönderme işlevselliği için Gmail SMTP sunucusuna bağlanır. E-posta ve şifre bilgilerinizi `send_email` fonksiyonunda belirtmeniz gerekmektedir.

3. **Persistence (Kalıcılık) Ekleme**:
   - `add_to_registry` fonksiyonu, script'i Windows kayıt defterine ekleyerek bilgisayar başlatıldığında otomatik olarak çalışmasını sağlar.

## Kullanım

1. Script'i çalıştırın. Bu adım, keylogger'ı başlatır ve tuş vuruşlarını kaydetmeye başlar.

```
py keylogger.py
```

2. Kaydedilen tuş vuruşları `log` değişkeninde biriktirilir.

3. Belirli aralıklarla (`thread_function` fonksiyonu ile ayarlanabilir), `log` değişkenindeki veriler belirtilen e-posta adresine gönderilir.

## Güvenlik Uyarısı

Bu script, yalnızca yasal amaçlarla ve yalnızca kendi bilgisayarınız veya izin verilen sistemlerde kullanılmalıdır. Başka kişilerin bilgilerini izinsiz olarak toplamak yasa dışı olabilir ve ciddi hukuki sonuçları olabilir. Script'in kullanımından kaynaklanabilecek yasa dışı veya kötü niyetli kullanımlardan dolayı, geliştirici veya dağıtıcı sorumlu tutulamaz.

---

Script, eğitim amacıyla ve yasal sınırlar içinde kullanılmak üzere geliştirilmiştir. Herhangi bir yasa dışı kullanımından dolayı sorumluluk kabul edilmez.
