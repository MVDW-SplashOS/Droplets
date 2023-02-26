import sys, os
import json

bas_version="0.0.1 in-dev"
bas_lang = "en-US"
command_type=""

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
			print("WIP")
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
