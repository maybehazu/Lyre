# 🗒️ WSL Tutorial
> 🎵 WSL (Windsong Lyre) is a sheet music language designed for creating macros for Genshin Impact's "Windsong Lyre".

+ The structure of a score in WSL has two headers, the first being "Info" which will provide the information that the performer must use for the build or execution process.
For example:
```
#Info
Type: 1 -> The "Type" property refers to how the song should be played, 1 means it will read each instruction as a key press, and 2 means it should read like sheet music.
Title: Bad Apple -> The "title" property is the name with which the .ahk file will be created in the build process.
Interval: 30 -> The "Interval" property refers to the speed at which the song will be played, the default value is "100", where a lower number means the song will be played faster and a higher number means the song will be played slower.
```

+ The "Song" header refers to the lyrics that should be interpreted according to the information provided in the "Info" header. For example:
```
#Song
H......... -> assuming the "Type" property is "1", this instruction will cause the "H" key to be pressed and then take a 9-point break.
fa......... -> Now, assuming the "Type" property is "2", this instruction will cause "fa" in bass clef to be pressed and then take a 9-point break.
(fa).... -> Now, assuming the "Type" property is "2", this instruction will cause you to press "fa" in the key of C and then take a 9-point break.
((fa)).... -> Now, assuming the "Type" property is "2", this instruction will cause you to press "fa" in treble clef and then take a 9-point break.
```
