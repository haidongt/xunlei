
from lixian import XunleiClient
from lixian_commands.util import *
from lixian_cli_parser import *
from lixian_config import get_config
import lixian_help
from getpass import getpass

@command_line_parser(help=lixian_help.login)
@with_parser(parse_login)
@with_parser(parse_logging)
def login(args):
	if args.cookies == '-':
		args._args['cookies'] = None
	if len(args) < 1:
		args.username = args.username or XunleiClient(cookie_path=args.cookies, login=False).get_username() or get_config('username') or raw_input('ID: ')
		args.password = args.password or get_config('password') or getpass('Password: ')
	elif len(args) == 1:
		args.username = args.username or XunleiClient(cookie_path=args.cookies, login=False).get_username() or get_config('username')
		args.password = args[0]
		if args.password == '-':
			args.password = getpass('Password: ')
	elif len(args) == 2:
		args.username, args.password = list(args)
		if args.password == '-':
			args.password = getpass('Password: ')
	elif len(args) == 3:
		args.username, args.password, args.cookies = list(args)
		if args.password == '-':
			args.password = getpass('Password: ')
	elif len(args) > 3:
		raise RuntimeError('Too many arguments')
	if not args.username:
		raise RuntimeError("What's your name?")
	if args.cookies:
		print 'Saving login session to', args.cookies
	else:
		print 'Testing login without saving session'
	import lixian_verification_code
	args.verification_code_path = "/Users/haidong.tang/Code/xunlei-lixian/a"
        verification_code_reader = lixian_verification_code.default_verification_code_reader(args)
	assert verification_code_reader != None
        XunleiClient(args.username, args.password, args.cookies, login=True, verification_code_reader=verification_code_reader)
