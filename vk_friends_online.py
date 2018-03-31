import vk
import getpass


APP_ID = '6113971'


def get_user_login():
    return input('Login: ')


def get_user_password():
    user_password = getpass.getpass('Password: ')
    return user_password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, v='5.73')
    online_friends_ids = api.friends.getOnline()
    friends_online = api.users.get(
        user_ids=online_friends_ids,
        fields="first_name,last_name",
    )
    return list(friends_online)


def output_friends_to_console(friends_online):
    print('Now online:')
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
