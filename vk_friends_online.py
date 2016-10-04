import vk
import getpass


APP_ID = 5651126


def get_user_login():
    login = input('Пожалуйста, введите логин пользователя: ')
    return login


def get_user_password():
    password = getpass.getpass('Пожалуйста, введите пароль пользователя: ')
    return password


def get_api(login, password):
    friends = 2
    session = vk.AuthSession(app_id=APP_ID, user_login=login,
                             user_password=password, scope=friends)
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
    login = get_user_login()
    password = get_user_password()
    api = get_api(login, password)

    friends_online = get_online_friends(api)
    output_friends_to_console(api, friends_online)
