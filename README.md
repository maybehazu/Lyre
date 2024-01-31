# 🎹 Lyre - Genshin Impact

<img src="https://github.com/nothazu/Lyre/assets/153567247/a5006f90-a6f2-488c-84b9-8c9073929a97" alt="Windsong lyre from genshin impact" align="right">

> ⭐ A tool that makes it easy to create macros for the genshin impact windsong lyre.

❗This project is still in development so it might have some performance issues. 

🧲 *The lyre interpreter is under development so I recommend building the macros in .ahk files to obtain better results.*

# 💫 Features
+ ✨ **Open source and free to use:** You can do whatever you want with the code in this project, even improve it or implement it in other projects for free.

+ 🍫 **Easy to use:** Lyre is an easy-to-use tool, plus it has a tutorial and an example for creating songs in the "songs" folder.

+ 🍃 **Multiple choices:** The program provides options to build your macros in .ahk files or run them directly with the Lyre interpreter and possibly have more options in the future.

# 💻 Requirements
+ [Have python installed](https://www.python.org/)
+ Windows 7 or above

# 📖 Instructions

+ Configure the "config.ini" file to customize the keys the program will work with and the build settings.
```ini
[input]
START_KEY=P #The key that runs the macro
END_KEY=O #The key with which the macro is paused
CLOSE_KEY=F1 #The key with which the macro is closed

[build]
PATH=build/ #The path where the .ahk files will be built (I recommend leaving it like this)
```

+ Run the file "install.bash".

+ Run the "Main.py" file and select the option of your preference.
> ![image](https://github.com/nothazu/Lyre/assets/153567247/bc1a0e91-1c7d-401d-8201-a2886678db3f)

+ The program will automatically find and list .wsl files in the "songs" path, choose the file you want to run / build.
> ![image](https://github.com/nothazu/Lyre/assets/153567247/a743362e-2e02-4cea-b6d7-e1ec06430730)

+ With the build option the program will create a macro in the path specified in the "config.ini" file.
> ![image](https://github.com/nothazu/Lyre/assets/153567247/b1a9d44b-d50b-408b-b947-510668a3219b)

+ With the option to run with Lyre, the Lyre interpreter will run and execute actions according to your configuration.
> ![image](https://github.com/nothazu/Lyre/assets/153567247/e9b0a8ec-502b-4f9e-b6ec-1636a37c26fc)


