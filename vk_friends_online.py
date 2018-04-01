import vk
import getpass
import sys


APP_ID = '6113971'


def get_user_login():
    return input('Login: ')


def get_user_password():
    user_password = getpass.getpass('Password: ')
    return user_password


def get_online_friends(login, password, api_version='5.73'):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, v=api_version)
    online_friends_ids = api.friends.getOnline()
    friends_online = api.users.get(
        user_ids=online_friends_ids,
        fields="first_name,last_name",
    )
    return friends_online


def output_friends_to_console(friends_online):
    print('Now online:')
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    try:
        login = get_user_login()
        password = get_user_password()
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        sys.exit('Ошибка авторизации, неверный логин или пароль.')
    output_friends_to_console(friends_online)
