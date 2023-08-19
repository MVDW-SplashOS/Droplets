import sys, os
import json
import requests
import whois

bas_version = "0.0.1 in-dev"
bas_lang = "en-US"
command_type = ""

#repositories = ["https://www.enthix.net/SplashOS/repo", "https://www.sdsadasdasasfdgfsasd.nl", "https://www.enthix.net/aaaaaa",  "https://www.watchcreo.com", "https://www.enthix.net/SplashOS/repo2", "https://www.enthix.net/SplashOS/repo3"]
repositories = ["https://www.enthix.net/SplashOS/repo", "https://www.enthix.net/SplashOS/repo2", "https://www.enthix.net/SplashOS/repo3"]

def main(argv):
	if(len(argv) == 0):
		print_help()
		sys.exit(os.EX_OK)

	read_configuration()

	command_type=argv[0]

	match command_type:
		case "-h" | "--help" | "help" | "h":
			print_help()
		case "-v" | "--version" | "version" | "v":
			print(f"{color.HEADER} > BAS version {bas_version} {color.ENDC}")
		case "-i" | "--install" | "install" | "i":
			install(argv)
		case _:
			print("Unknown argument, please do `bas --help` for help")
	
def print_help():
	doc_help_file=open(resolve_path("lang/" + bas_lang + "/doc_help.txt"), 'r')
	doc_help_content = doc_help_file.read()
	print(doc_help_content)
	doc_help_file.close()

def resolve_path(path):
	return os.path.join(os.path.abspath(os.path.dirname(__file__)), path)

def read_configuration():
	configuration_path_name = "/etc/bas/"
	configuration_file_name = "config.json"
	os.makedirs(configuration_path_name, exist_ok=True)

	if os.path.exists(configuration_path_name + configuration_file_name):
		# TODO: Read out config file
		config_file = open(configuration_path_name + configuration_file_name, "r")
		config_data = json.loads(config_file.read())
		if config_data["config_version"] != 1:
			print(f"{color.FAIL}ERROR: Configuration version doesn't match the required version.\nTo fix this you need to manually upgrade your configuration file in /etc/bas/config.json{color.ENDC}")
			sys.exit(os.EX_CONFIG)
		config_file.close()
	else:
		create_config()


def create_config():
	default_config_file=open(resolve_path("default_config.json"), 'r')
	default_config_content = default_config_file.read()
	config_file = open("/etc/bas/config.json", "a")
	config_file.write(default_config_content)
	config_file.close()
	default_config_file.close()



def install(args):
	print(f"{color.HEADER}[🔍] Searching repositories for package '{args[1]}'");
	i = 0
	for repo in repositories:
		i = i + 1

		#try :
			#whois.whois(repo)
			
		#except (whois.parser.PywhoisError):
		#	print(f"{color.FAIL}ERROR: The repo domain '{repo}' does not exist, please check configuration for any typos in the domain name.{color.ENDC}")
		#	sys.exit(os.EX_NOHOST)

		repo_info = requests.get(repo, timeout=10)

		symbol = "┣━"
		if i == len(repositories):
			symbol = "┗━"

		if repo_info.status_code == 200:

			print(f"     {symbol} Checking {repo_info.json()['NAME']}.")
		else:
			print(f"     {symbol} Something went wrong checking repo {repo}")





def check_domain_exists(domain):
    try:
        response = requests.head(f'{domain}')
        return response.status_code == 200
    except requests.ConnectionError:
        return False

class color:
	HEADER = '\033[94m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


if __name__ == "__main__":
	main(sys.argv[1:])
