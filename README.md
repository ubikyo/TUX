# TUX
Terminal enhancement for Ubuntu.

> [!NOTE]
> Successfully tested on **Ubuntu 18** to **26+**.


# TUX.motd

[Awesome MOTD](https://github.com/ubikyo/TUX.motd/blob/main/README.md) for Ubuntu with system information and more.

<img src="https://raw.githubusercontent.com/ubikyo/TUX.motd/refs/heads/dev/ressources/motd.png" width="500">

## Parameters

Options for the `tux_motd` command:

| Option | Description |
|-|-|
| `--version` | Display the installed version (currently `1.1`) and exit |

# TUX.ps1

Nice optional PS1 prompt.

Powerline separators remain enabled whether or not Nerd Font icons are enabled.
Disabling Nerd Font icons hides only the Ubuntu logo block in the prompt.

<img src="https://raw.githubusercontent.com/ubikyo/TUX.ps1/refs/heads/dev/ressources/ps1.png" width="600">

# Prerequisites

TUX uses optional Nerd Fonts to display enhanced icons and symbols. To view these elements properly in your SSH terminal, you need to install a [Nerd Font](https://www.nerdfonts.com/font-downloads) (such as [Fira Code](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.5.1/FiraCode.zip), [DejaVuSans](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.5.1/DejaVuSansMono.zip), etc.) on your local machine. Nerd Fonts are standard fonts that have been patched to include over 10,000 icons from Font Awesome, Material Design, and more.

# Installation

## Automatic
All features will be installed (like the silent flag).

    curl -fs https://raw.githubusercontent.com/Ubikyo/TUX/refs/heads/main/install.sh | sudo bash -s -


## Manual
You will be prompted to select the features to install.

    curl -O https://raw.githubusercontent.com/Ubikyo/TUX/refs/heads/main/install.sh
    chmod +x ./install.sh
    sudo bash -i ./install.sh

> [!WARNING]
> Questions are shown when the installer runs in a terminal, unless `--silent` is used. Without a terminal (for example, when piping the script into Bash), all options are accepted automatically.


## Parameters

| Option | Description |
|-|-|
| `--silent` | Disable all questions and enable all features |
| `--help` | Show the helper and exit |

  
# Update

    cd /opt/TUX/repo
    git pull
    sudo bash -i ./install.sh