"""тест Pylint"""
import subprocess
import time

import psutil


def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()


def main():
    """тест Pylint"""
    process = []

    while True:
        time.sleep(1)
        action = input(
            'Выберите действие: q - выход, '
            'x - закрыть все окна, '
            's - запустить сервер, '
            'k - запустить клиенты:')
        if action == 's':
            # Запускаем сервер!
            process.append(
                subprocess.Popen(
                    'python server.py', shell=True))
        elif action == 'k':
            print('Убедитесь, что на сервере зарегистрировано необходимо количество (от 2 шт.) '
                  'тестовых клиентов с паролем 123456.')
            print('Первый запуск может быть достаточно долгим из-за генерации ключей!')
            clients_count = int(
                input('Введите количество тестовых клиентов для запуска: '))
            # Запускаем клиентов:
            for i in range(clients_count):
                process.append(
                    subprocess.Popen(
                        f'python client.py -n test{i + 1} -p 123456', shell=True))
        elif action == 'x':
            while process:
                kill(process.pop().pid)
            print('Все окна закрыты!')
        elif action == 'q':
            print('Работа программы завершена!')
            break


if __name__ == '__main__':
    main()
