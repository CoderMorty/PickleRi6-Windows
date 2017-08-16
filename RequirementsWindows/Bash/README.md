# Install Bash by Blank
## Install the Windows Subsystem for Linux
1. Run the PowerShell script file, in this directory.
2. Restart your computer when prompted.


## For Windows Insiders: Install Linux distribution of choice
> This section is for Windows Insiders (build 16215 or later). Follow these steps to Check your build. For earlier versions of Windows 10, follow [these instructions using lxrun](https://msdn.microsoft.com/en-gb/commandline/wsl/install_guide#for-anniversary-update-and-creators-update-install-using-lxrun).


1. Open the Windows Store and choose your favorite Linux distribution. Here are links directly to the store installers (I'd recommend Ubuntu):
  * [Ubuntu](https://www.microsoft.com/store/p/ubuntu/9nblggh4msv6)
  * [OpenSUSE](https://www.microsoft.com/store/apps/9njvjts82tjx)
  * [SLES](https://www.microsoft.com/store/apps/9p32mwbh6cns)
  
![Ubuntu - Windows Store](https://i-msdn.sec.s-msft.com/en-us/commandline/wsl/media/ubuntustore.png)


2. Select "Get"
> **Troubleshooting: Installation failed with error 0x80070003**
> The Windows Subsystem for Linux only runs on your system drive (usually this is your C: drive). Make sure that new apps are stored on your system drive.
> Open **Settings** -> **Storage** -> **More Storage Settings: Change where new content is saved**
> ![Settings - New Apps](https://i-msdn.sec.s-msft.com/en-us/commandline/wsl/media/appstorage.png)


3. Once the download has completed, select "Launch".
This will open a console window. Wait for installation to complete then you will be prompted to create your UNIX user account.
![Starting Ubuntu](https://i-msdn.sec.s-msft.com/en-us/commandline/wsl/media/ubuntuinstall.png)
> **Troubleshooting: Installation failed with error 0x8007007e**
> This error occurs when your system doesn't support Linux from the store. Make sure that:
>  * You're running Windows build 16215 or later. [Check your build](https://msdn.microsoft.com/en-gb/commandline/wsl/install_guide#prerequisites).
>  * The Windows Subsystem for Linux optional component is enabled. [Instructions here](https://msdn.microsoft.com/en-gb/commandline/wsl/install_guide#Install-the-Windows-Subsystem-for-Linux).

4. Create your UNIX username and password. This user account can be different from, and has no relationship to, your Windows username and password. [Read more](https://msdn.microsoft.com/en-us/commandline/wsl/user_support).


You're done! Now you can use your Linux environment.




