### Как установить
- [Windows](https://git-scm.com/download/win/)
- [Linux](https://git-scm.com/download/linux)
- [MacOS](https://git-scm.com/download/mac)

### Как создать SSH ключ
```bash
ssh-keygen -t rsa -b 2048
```
Создает ключ типа `rsa` размером 2048 байт.

### Первые шаги
```bash
git config --global user.name "Ch0p1k3"
git config --global user.email "ch00p.228@gmail.com"
```
Установка имени и email, который будет отображаться в истории git.

### Базовые команды
- `git init` - инициализация репозитория;
- `git clone` - клонирование репозитория;
- `git add` - добавление файла в индекс;
- `git commit` - сделать коммит;
- `git status` - статус файлов в индексе;
- `git log` - лог со всеми сделанными коммитами;
- `git checkout` - переключение на другую ветку или сброс изменений в файле;
- `git branch` - вывести список веток и посмотреть на какой ты сейчас находишься;
- `git revert` - откатить коммит локально;
- `git merge` - мердж веток;
- `git pull` - подтянуть изменения из ветки;
- `git push` - залить изменения на удаленный репозиторий;

### Полезные ссылки
- [Git Pro](https://git-scm.com/book/en/v2) - книга по git, есть на русском
- [Классный тренажер](https://gitexercises.fracz.com/)
