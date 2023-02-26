import sys

bas_version="0.0.1 in-dev"
bas_lang = "en-US"

def main(argv):
	operation=argv[0]
	match operation:
		case "-h" | "--help" | "help" | "h":
			print_help()
		case "-v" | "--version" | "version" | "v":
			print(f"{color.HEADER} > BAS version {bas_version} {color.ENDC}")
		case "-i" | "--install" | "install" | "i":
			print("WIP")
		case _:
			print("Unknown argument, please do `bas --help` for help")
	
def print_help():
	doc_help_file=open("./lang/" + bas_lang + "/doc_help.txt", 'r')
	doc_help_content = doc_help_file.read()
	print(doc_help_content)
	doc_help_file.close()
	
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
