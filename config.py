# Qtile Configuration File
# Andrea Villar - 2024
# Kinder.Dots Project

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Color scheme
colors = {
    "background": "#F7F7F7",
    "foreground": "#000000",
    "accent": "#007AFF",
    "highlight": "#E5E5EA"
}

# Mod key and terminal
mod = "mod4"
terminal = "alacritty"
control = "control"

# Keybindings
keys = [
    # Window navigation
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Window movement
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Window resizing
    Key([mod, control], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, control], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, control], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, control], "k", lazy.layout.grow_up(), desc="Grow window up"),

    # Layout and window management
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Qtile management
    Key([mod, control], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, control], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Application launchers
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Open application menu"),
    Key([mod], "n", lazy.spawn("rofi-noter"), desc="Open noter"),
    Key([mod, "shift"], "p", lazy.spawn("bwmenu"), desc="Open password manager"),
    Key([mod, "mod1"], "space", lazy.spawn("rofi-web"), desc="Open web search"),

    # Window navigation
    Key([mod, "shift"], "m", lazy.spawn("rofi -show"), desc="Show window switcher"),

    # Volume control
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Lower volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Raise volume"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Mute/unmute volume"),

    # Brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Decrease brightness"),

    # Media control
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next track"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous track"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/pause"),
]

# Virtual terminal switching (for Wayland)
for vt in range(1, 8):
    keys.append(
        Key(
            [control, "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

# Workspace groups
groups = [Group(i) for i in [
    "   ", "   ", "   ", "   ", "  ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        Key([mod], actual_key, lazy.group[group.name].toscreen(), desc=f"Switch to group {group.name}"),
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name), desc=f"Move focused window to group {group.name}")
    ])

# Layouts
layouts = [
    layout.Columns(
        border_focus="#8d67de",
        border_focus_stack=["#ffffff", "#000000"],
        border_normal="#000000",
        border_width=3
    ),
    layout.Max(
        border_focus="#8d67de",
        border_focus_stack=["#ffffff", "#000000"],
        border_normal="#000000",
        border_width=3
    ),
    layout.MonadTall(
        border_focus="#8d67de",
        border_focus_stack=["#ffffff", "#000000"],
        border_normal="#000000",
        border_width=3
    ),
]

# Widget defaults
widget_defaults = dict(
    font="Iosevka Nerd Font",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Screens and bars
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=colors["accent"],
                    inactive=colors["foreground"],
                    highlight_method="line", 
                    this_current_screen_border=colors["accent"],
                    this_screen_border=colors["highlight"],
                    other_current_screen_border=colors["background"],
                    other_screen_border=colors["background"],  
                    foreground=colors["foreground"],
                    background=colors["background"],
                ),
                widget.Prompt(),
                widget.WindowName(foreground=colors["foreground"]),
                widget.Battery(format=" 󰁹 {percent:2.0%} |", foreground=colors["foreground"]),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"), 
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),  
                widget.Clock(format='| %d/%m/%Y - %H:%M |', foreground=colors["foreground"]),
                widget.QuickExit(default_text='󰤁 |', countdown_format='[{}]', foreground=colors["foreground"]),
            ],
            24,  
            background=colors["background"],
            opacity=0.9,
        ),
    ),
]

# Mouse bindings
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Other configurations
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"
