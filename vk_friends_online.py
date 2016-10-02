import vk
import argparse


APP_ID = 5651126


def createParser():
    parser = argparse.ArgumentParser(usage='%(prog)s [аргументы]',
                                     description="Вывод друзей в VK, "
                                                 "кто онлайн, "
                                                 "с помощью %(prog)s")
    parser.add_argument('-l', '--login', nargs='?', help="Логин пользователя")
    parser.add_argument('-p', '--password', nargs='?', help="Пароль пользователя")
    return parser


def get_user_login(namespace):
    login = namespace.login
    if not login:
        login = input('Пожалуйста, введите логин пользователя: ')
    return login


def get_user_password(namespace):
    password = namespace.password
    if not password:
        password = input('Пожалуйста, введите пароль пользователя: ')
    return password


def get_api(login, password):
    session = vk.AuthSession(app_id=APP_ID, user_login=login,
                             user_password=password, scope=2)
    return vk.API(session)


def get_online_friends(api):
    friends_online_ids = api.friends.getOnline()
    friends_online_info = api.users.get(user_ids=friends_online_ids)
    return friends_online_info


def output_friends_to_console(api,friends_online):
    print("Список ваших друзей, кто Онлайн:")
    for friend in friends_online:
        print(friend['first_name'],friend['last_name'])


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    login = get_user_login(namespace)
    password = get_user_password(namespace)
    api = get_api(login, password)

    friends_online = get_online_friends(api)
    output_friends_to_console(api, friends_online)
