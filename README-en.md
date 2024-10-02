# Qtile Configuration for Kinder.Dots

This repository contains the Qtile configuration used in the Kinder.Dots project. Qtile is a highly customizable tiling window manager written and configured in Python.

## Features

- Customized color scheme for a visually appealing interface
- Efficient keybindings for window management and navigation
- Personalized workspace groups with unique icons
- Integration with various applications like Rofi, Alacritty, and system controls

## Installation

To use this configuration:

1. Ensure Qtile is installed on your system
2. Clone this repository into your Qtile config directory:

```bash
git clone https://github.com/AndreaKinder/Kinder.Qtile.git
sudo mv Kinder.Qtile/* ~/.config/qtile
```

1. Restart Qtile or log out and log back in

## Key Bindings

Here are some of the most important key bindings:

| **Keybinding** | **Action** |
| --- | --- |
| [mod] + h/j/k/l | Move focus between windows |
| [mod] + [shift] + h/j/k/l | Move windows within the layout |
| [mod] + Return | Launch terminal |
| [mod] + w | Close focused window |
| [mod] + m | Open application menu |
| [mod] + (1-6) | Switch to workspace group |

For a full list of keybindings, please refer to the `keys` section in the `config.py` file.

## Customization

Feel free to modify the `config.py` file to suit your preferences. You can change colors, layouts, widgets, and keybindings to create your perfect desktop environment.

## Dependencies

This configuration relies on several additional packages:

- Alacritty (terminal emulator)
- Rofi (application launcher)
- Pactl (volume control)
- Brightnessctl (brightness control)
- Playerctl (media player control)

Ensure these are installed for full functionality.

## Contributing

Contributions to improve this configuration are welcome. Please feel free to submit issues or pull requests.

## License

This Qtile configuration is part of the Kinder.Dots project and is released under the MIT License. See the LICENSE file for more details.

## Acknowledgements

This configuration is part of the larger Kinder.Dots project. For more information about the overall project, please refer to the main [Kinder.Dots repository](https://github.com/YourUsername/Kinder.Dots).
