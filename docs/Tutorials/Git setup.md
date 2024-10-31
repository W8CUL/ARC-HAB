
## After installing git

- Open a folder in windows explorer where you want the files to be saved
- Right click and select "Git Bash here"
- On the command window try the following commands
	- `ssh-keygen -t ed25519`
	- `ls ~/.ssh/`
	- If you see files with names `id_ed25519` and `id_ed25519.pub` they public/private key pairs have been generated correctly
	- `git config --global user.email "<email>"`
	- `git config --global user.name "<first last name>"`
	- to check the settings type `git config list`  and check if you see your email and username
	- `cat ~/.ssh/id_ed25519.pub` and copy the full text you see
	- Open https://github.com/settings/keys
		- Click on "New SSH Key"
		- Paste the text and give it a suitable name
	- We are done with configuration. You don't have to do these ever again.
- Let go to the project page https://github.com/W8CUL/ARC-HAB/
	- Click on the "Code" (Green Icon)
	- Make sure to select ssh
- Go back to the terminal
	- `git clone <repo-location>`

