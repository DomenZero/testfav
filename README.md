# testfav
Автотест для **[сайта](https://sfbay.craigslist.org/d/jobs/search/jjj)** . Проверяет наличие верхнего поста в избранном.

## Быстрый запуск под Windows.
1. Скачать, установить **[Chrome](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en)**
2. Скачать и скопировать **[chromedrive.exe](https://sites.google.com/a/chromium.org/chromedriver/)** в **C:\webdrivers**
3. Скопировать себе на ПК из репозитория **testfav_tests\dist\fav_test**
4. Запустить из консоли **fav_test.exe**
5. Выбрать объявление на добавление в избранное
6. Результат проверки, либо положительный "First post is favorites", либо отрицательный "First post isn't favorites".

## Запуск с помощью python в venv.
1. Скачать, установить **[Chrome](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en)**
2. Скачать и скопировать **[chromedrive.exe](https://sites.google.com/a/chromium.org/chromedriver/)** в **C:\webdrivers** 
3. Скопировать себе на ПК репозиторий.
4. Установить [Python 3](https://www.python.org/downloads/windows/).
5. Находясь в папке со скачанными файлами **testfav_env** и **testfav_tests**. Запустить **virtualvenv**. 
Для этого в консоле ввести: `testfav_env\Scripts\activate.bat`
6. Оставаясь в консоли, запустить тест: `python fav_test.py`
7. Выбрать объявление на добавление в избранное.
8. Результат проверки, либо положительный "First post is favorites", либо отрицательный "First post isn't favorites".

