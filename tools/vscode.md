# Visual Studio Code

## Установка

Переходим по [ссылке](https://code.visualstudio.com/), скачиваем и устанавливаем.

## После установки

Открываем VSCode. Можно открыть директорию, в которой вы будете решать задачи - `File -> Open Folder`. Через левую менюшку можно создавать файлы: `ПКМ -> New file`. Запускать можно через кнопку ▶️ (только после установки плагина [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)).

## Плагины

Для комфортной жизни вам хватит следующих плагинов (можно почитать их описание):
- [Python Extension Pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack), для IntelliSense (Pylance), Linting;
- [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) для запуска питон скрипта из интерфейса `VsCode`.
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) для того, чтобы открывать тетрадки.
- [Sort lines](https://marketplace.visualstudio.com/items?itemName=Tyriar.sort-lines) - опционально, позволяет сортировать строки в файле. Надо выделить и нажать `F9`. Я в основном пользуюсь для того, чтобы сортировать импорты.

## Полезные комбинации клавиш

Вообще вот ссылка на все стандартные комбинации клавиш:
- [Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- [MacOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
- [Linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)

Вообще я не вижу сильной разницы между Linux и Windows, но зато есть существенная разница с MacOS. Я напишу классный комбинации сюда, пользуясь Linux/Windows клавиатурой, так как таких большинство. Начнем:
- `Ctrl + O` - открыть файл.
- `Ctrl + P` - перейти к файлу, если написать `:` и номер строки, то перейдете к строке.
- `Ctrl + Shift + P` - тоже самое, что `Ctrl + P` и написать `>`. Это откроет вам `command palette` (извиняйте русский перевод мне не нравится). Здесь можно перезагрузить окно - `Developer: Reload windows`, открыть настройки шорткатов `Preferences: Open Keyboard Shortcuts`, изменение темы `Preferences: Color Theme` и т.д. Также можно пользоваться штуками из плагинов, - просто начните писать название плагина и оно вам покажет, что доступно.
- `Ctrl + ЛКМ` по слову в коде или `F12` - часто говорят прямо на английском `Go to definition`, что в переводе и значит переход к определению чего-либо.
- `Ctrl + B` - открывает/закрывает левую панель.
- `Ctrl + ~` - открывает/закрывает терминал.
- `Ctrl + K Z` - включает/выключает Zen Mode. Также можно два раза нажать `Esc`, чтобы выйти.
- `Ctrl + Space` - автодополнение в коде.
- `F2` - рефакторинг - надо выделить нужную переменную и нажать F2, тогда можно будет переименовать ее везде (на самом деле неправда, но почти все переименовывает).
- `Ctrl + D` - выделите слово и нажмите эту комбинацию, тогда
- `Shift + Alt + F` - форматнуть документ. Нажмите эту комбинацию в `.py` файле, тогда расширение [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) предложит вам скачать один из форматеров. Я пользуюсь `black`, так как у нас им пользуются на работе. Таким образом можно будет быстро поправлять ваш код на `PEP8`.

## Открыть VSCode из терминала

```bash
code /home/chopik/python
```

То есть надо написать `code` и нужную директорию. Если директорию не указать, то по-умолчанию берется текущая. [Ссылка на базовые команды в терминале](terminal.md).
