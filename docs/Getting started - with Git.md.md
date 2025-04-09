# WVU ARC - High altitude ballooning(HAB) Documentation

This repository is used to maintain documentation that are generated from the ARC-HAB projects.

For wide usability [Obsidian-md](https://obsidian.md) is recommended as a cross platform interface for note taking. If you are an advanced user feel free to choose other options
## Setup instructions 

### Mac/linx

Git is used as the main method of syncing/sharing documentation and progress. 

1. Make a git account
2. Install git on your computer. (on mac/linux can be done on the cmd, on windows needs an installer)
3. generate ssh-keys: `ssh-keygen` press enter all the way. this will make a rsa key typically inside `~/.ssh`
4. add the ssh key to your git account. `cat ~/.ssh/id_rsa.pub` copy paste to your profile.
5. clone the repo using the ssh link: `git clone git@github.com:W8CUL/ARC-HAB.git`
   
- Recommend using and setting up [obsidian-md](https://obsidian.md/) (this is a free note taking tool and you only need to install it most of the configuration is done to work with git and other requirements)
- A good tutorial for basic markdown syntax can be found [here](https://www.markdownguide.org/basic-syntax/)

### Windows 
*Last tested in 2018 on win 10. Need to check and update*

1. Make an account at [https://github.com/](https://gitlub.com/) use a suitable name.
2. Install Notepad++ using the following link [https://notepad-plus-plus.org/downloads](https://notepad-plus-plus.org/downloads) (VS code might work too. Change accordingly)
3. Download and install **git desktop** [https://git-scm.com/download/win](https://git-scm.com/download/win)

#### Git bash install instructions 

1. Remove **Git GUI Here**
2. Select Notepad++ as the default editor (option 2)
3. Keep all the other options the same

Once the installation is complete if you right click on any folder the context menue should show `Git Bash Here` options

#### Adding SSG key to github

1. Login and https://github.com/settings/keys
2. Open a git bash window and execute the following commands
   
``` bash
ssh-keygen
ls ~/.ssh  
cat ~/.ssh/id_rsa.pub
```

- The commands will make a ssh public and private key pair and save in your virtual home under the `.ssh` folder.
- The `id_rsa.pub` file content will be displayed if everything works and you can copy this key and use it and add to your account

## Getting started with documentation - Video tutorial

An easy to follow tutorial can be found [here]()(pending)
test git on arc pc


