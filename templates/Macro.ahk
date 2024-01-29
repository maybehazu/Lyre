Hotkey, [key1], ToggleMacro

macro := False

ToggleMacro:
    if (macro) {
        Goto, StopMacro
    } else {
        Goto, StartMacro
    }

StartMacro:
    Hotkey, [key1], Init
    macro := True
    Return

StopMacro:
    Hotkey, [key1], Off
    macro := False
    Return

Init:
[song]

    SetTimer, DisableMacro, -1
    Return

DisableMacro:
    Hotkey, [key1], On
    Return

[key2]::Reload