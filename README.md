# lab03os_analis

Проаналізувати частотну характеристику (частотний розподіл) розміру файлів у файловій системі на вашому комп'ютері (залежність кількості файлів від їх розміру). 
Надати звіт: 
1) підготовка даних: як саме збирали дані про розподіл для аналізу
* hint: це можна зробити одним командним рядком у ОС (find / ls + grep + awk + > result.txt)
2) власне аналіз та візуалізація залежностей 
* hint: гістограма кількості файлів (Oy) залежно від їх розміру (Ox) - гарна відправна точка, але цього явно недостатньо
3) висновки
* hint: гарний висновок – "переважна більшість файлів (х%) має розміри у діапазоні від a до b", де x - якомога більше (75-80-85-90%), а [a, b] – якомога вужчий проміжок

Hint: краще брати всю файлову систему (або принаймні системний диск, а не лише 1 каталог).

Прикріпити звіт, який відображає всі 3 пункти для вашої файлової системи
