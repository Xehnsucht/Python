import os
import zipfile
import time
from typing import List


def zipZip():
    source = ['D:\\Book']
    # Заметьте, что для имён, содержащих пробелы, необходимо использовать
    # двойные кавычки внутри строки.
    # 2. Резервные копии должны храниться в основном каталоге резерва.
    target_dir = 'D:\\Backup'  # Подставьте ваш путь.
    # 3. Файлы помещаются в zip-архив.
    # 4. Именем для zip-архива служит текущая дата и время.
    today = target_dir + os.sep + time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')
    # Комментарий к архиву
    comment = input('Enter commentary ---> ')

    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' + '.zip' + \
                 comment.replace(' ', '_')

    with zipfile.ZipFile(target_dir, mode='a',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in source:
            add_file = os.path.join(source, file)
            zf.write(add_file)

    os.system(target)
    pass


def osZip():
    # 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
    source = ['D:\\Work\\Meas\\Test']
    # Заметьте, что для имён, содержащих пробелы, необходимо использовать
    # двойные кавычки внутри строки.
    # 2. Резервные копии должны храниться в основном каталоге резерва.
    target_dir = 'D:\\Work\\ZipMeas'  # Подставьте ваш путь.
    # 3. Файлы помещаются в zip-архив.
    # 4. Именем для zip-архива служит текущая дата и время.
    today = target_dir + os.sep + time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')
    # Комментарий к архиву
    comment = input('Enter commentary ---> ')
    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' + \
                 comment.replace(' ', '_') + '.zip'

    # Создание каталога, если его еще нету
    if not os.path.exists(today):
        os.mkdir(today)
        print('Каталог успешно создан', today)

    # 5. Используем команду "zip" для помещения файлов в zip-архив
    zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

    # Запускаем создание резервной копии
    if os.system(zip_command) == 0:
        print('Резервная копия успешно создана в', target)
    else:
        print('Создание резервной копии НЕ УДАЛОСЬ')


if __name__ == "__main__":
    osZip()
    # zipZip()
