# BAS - Bash Applications & Services
The package manager designd only for command line based applications or services.

## How to use BAS?
BAS is designed to be as easy to use as something like `apt` or `dnf`.

### Managing applications: 
Install application: `bas install <package name>`

Remove application: `bas remove <package name>`

Update all applications: `bas update`

List all aplications: `bas list`

### Managing repositorys:
Add repository: ``bas repo add <url>``

Remove repository: ``bas repo remove <url>``

List all repositorys: `bas repo list`

## Building BAS from source
Building BAS requires Python 3.6+ and pip to be installed on your system.

### Debian/Ubuntu based distros:
  1. `sudo apt update`
  1. `sudo apt install python3 python3-pip`
  2. `pip3 install pyinstaller`
  3. `./build.sh`

### Fedora/RHEL based distros:
  1. `sudo dnf install python3-pip`
  2. `pip install pyinstaller`
  3. `./build.sh`
