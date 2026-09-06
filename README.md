# TUX
Terminal enhancement for Ubuntu.

> [!NOTE]
> Successfully tested on **Ubuntu 18** to **26+**.


# TUX.motd

[Awesome MOTD](https://github.com/ubikyo/TUX.motd/blob/main/README.md) for Ubuntu with system information and more.

<img src="https://raw.githubusercontent.com/ubikyo/TUX.motd/refs/heads/dev/ressources/motd.png" width="500">

# TUX.ps1

Nice optional PS1 prompt.

<img src="https://raw.githubusercontent.com/ubikyo/TUX.ps1/refs/heads/dev/ressources/ps1.png" width="600">

# Prerequisites

TUX uses optional glyphs (icons) to display some informations. To view these elements properly in your SSH terminal, you need to install a [Nerd Font](https://www.nerdfonts.com/font-downloads) (such as [Fira Code](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.5.1/FiraCode.zip), [DejaVuSans](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.5.1/DejaVuSansMono.zip), etc.) on your local machine. Nerd Fonts are standard fonts that have been patched to include over 10,000 icons from Font Awesome, Material Design, and more.

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
> You need to start the installer as an interactive user (**bash -I**). If you don't, no dialogs will be shown.


## Parameters

| Option | Description |
|-|-|
| `--silent` | Disable all questions and enable all features |
| `--help` | Show the helper and exit |

  
# Update

    cd /opt/TUX/repo
    git pull
    sudo bash -i ./install.sh