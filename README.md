# medyatakip
Django framework ile oluşturulmuş medya bilgilindirme sistemi.
## Kurulum
https://www.python.org/ sitesinden python son sürümü indirip kurun.
> **Dikkat** Add python * to PATH seçeneğini işaretlemeyi unutmayın

### Pip
Klonladığınız dosyanın içinde cmd veya powershell açıp aşağıdaki komutu girin
```
pip install -r requirements.txt
```
### Database oluşturmak 
```
python manage.py makemigrations
```
```
python manage.py migrate
```

### Projeyi Çalıştırmak
```
python manage.py runserver
```
