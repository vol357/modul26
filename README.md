"# modul26" 
запуск с помощью run_test_26_1.bat
в файле log.txt видно результат выполнения - ошибка при импорте в строке:
from pages.auth_page import AuthPage
E   ModuleNotFoundError: No module named 'pages'

то есть мы не можем перейти в другой каталог!
если мы расположим файлы, из которых импортируются классы и пр., в папке с самим тестом и отредактируем соответствушие строки,
то выскочит другая ошибка - про использование библиотеки URLLIB3:
from urllib3.parse import urlparse
E   ModuleNotFoundError: No module named 'urllib3.parse'
