from argparse import ArgumentParser
from platform import win32_ver, mac_ver, linux_distribution
import requests


URI = 'https://murmuring-stream-99222.herokuapp.com/posts'


def get_args():
    parser = ArgumentParser(description='Fake git command')
    subparsers = parser.add_subparsers()
    parser_list = subparsers.add_parser('list', help='show list')
    parser_list.set_defaults(handler=show_list)
    parser_push = subparsers.add_parser('push', help='push message')
    parser_push.add_argument('path_root_src', help='message')
    parser_push.set_defaults(handler=push_message)
    return parser.parse_args()


def show_list(args):
    response = requests.get(URI)
    posts = response.json()
    for post in posts:
        print(post['command'], post['message'])


def get_env():
    if win32_ver() != ('', '', '', ''):
        return "Windows"
    if mac_ver() != ('', ('', '', ''), ''):
        return "MacOS " + str(mac_ver()[0])
    if linux_distribution() == ('', '', ''):
        return str(linux_distribution()[0]) + " " + str(linux_distribution()[1])


def push_message(args):
    data = {
        'command': get_env(),
        'message': args.path_root_src
    }
    response = requests.post(URI, data=data)


def main():
    args = get_args()
    if hasattr(args, 'handler'):
        args.handler(args)


if __name__ == '__main__':
    main()