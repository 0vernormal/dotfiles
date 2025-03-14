#########################################
#########  importable things  ###########
#########################################

import os
import subprocess
import json
import psutil
from libqtile import bar, layout, qtile, widget, extension, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.bar import Bar
from types import FunctionType

#if qtile-extra is installed on the system, the following ones will work, if not, the config will not work.
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget import StatusNotifier


###colors###
from colors import GruvboxDark, Everforest, Gray, DarkTerminalGreen

colors = GruvboxDark


#########################################
#############  variables  ###############
#########################################


mod = "mod4"
mod1 = "mod1"

terminal = "alacritty"
rofi_app_launcher = "rofi -show drun -show-icons"
zen = "zen-browser"
tor_browser = "bash /home/overnormal/apps/tor-browser/Browser/start-tor-browser"
virt_manager = "/usr/bin/virt-manager"
file_manager = "thunar"
screenshot = "flameshot gui"
lock = "i3lock-fancy -gpf Cantarell"
powermenu = "rofi -show power-menu -modi power-menu:rofi-power-menu"
wallselector = "bash /home/overnormal/.config/rofi/wallpaperselector.sh"
remnote = "/home/overnormal/apps/RemNote-1.18.43.AppImage"


def clipboard(qtile):
    subprocess.Popen(["python3", "/home/overnormal/.config/rofi/roficopyq.py"])


def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read()) / 1000  
            return f"{temp:.1f}°C"
    except:
        return "N/A"

def cpu_info():
    try:
        temp = get_cpu_temp()
        usage = psutil.cpu_percent()
        return f" {usage}% |  {temp}"
    except:
        return "N/A"


#########################################
#############    hooks     ##############
#########################################


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])

@hook.subscribe.group_window_add
def switchtogroup(group, window):
    group.toscreen()

@hook.subscribe.startup_once
def start_once():
    subprocess.Popen(["copyq"])


#########################################
#############     keys      #############
#########################################


keys = [
    #focus settings for windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod1], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod1, "shift"], "Tab", lazy.layout.previous(), desc="Move window focus to previous window"),

    #moving settings for windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    #growing settings for windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),


#personal shortcuts
Key([mod1], "1", lazy.spawn(file_manager), desc="Launch Thunar file manager"),
Key([mod1], "2", lazy.spawn("floorp"), desc="Launch Zen browser"),
Key([mod1], "3", lazy.spawn("thorium-browser"), desc="Launch thromium browser"),
Key([mod1], "4", lazy.spawn(virt_manager), desc="Launch Virt Manager"),
Key([mod1], "5", lazy.spawn(remnote), desc="launch remnote"),
Key([mod1], "9", lazy.spawn(tor_browser), desc="tor"),
Key([mod], "m", lazy.spawn("quodlibet"), desc="launch quod libet"),
Key([mod, "shift"], "s", lazy.spawn(screenshot), desc="Take a screenshot with Flameshot"),
Key([mod1, "shift"], "l", lazy.spawn(lock), desc="Lock screen using i3lock-fancy"),
Key([mod1, "shift"], "t", lazy.spawn("setxkbmap tr"), desc="Switch to Turkish keyboard layout"),
Key([mod1, "shift"], "u", lazy.spawn("setxkbmap us"), desc="Switch to US keyboard layout"),
Key([mod1, "shift"], "p", lazy.spawn(powermenu), desc="rofi power menu"),
Key([mod, mod1], "v", lazy.function(clipboard), desc="rofi copyq menu"),
Key([mod], "w", lazy.spawn(wallselector), desc="wallpaper selector"),
Key([mod], "i", lazy.spawn("alacritty -e btop"), desc="launch btop"),

    Key([mod, "shift"], "Return", lazy.spawn("cool-retro-term"), desc="cool retro term"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod1], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window" ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="rofi"),


#brightness buttons
Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +7%"), desc="Increase screen brightness"),
Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 7%-"), desc="Decrease screen brightness"),

#vol buttons
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
]



#########################################
########   Groups / Workspaces   ########
#########################################


group_names = [
    ("1", "󰬺"),
    ("2", "󰬻"),
    ("3", "󰬼"),
    ("4", "󰬽"),
    ("5", "󰬾"),
    ("6", "󰬿"),
    ("7", "󰭀"),
    ("8", "󰭁"),
    ("9", "󰭂"),
    ("0", "󰿩")
]


groups = [Group(name, label=icon) for name, icon in group_names]

for i in groups:
    keys.extend(
         [
             Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
             Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Move window & switch to group {i.name}"),
         ]
    )

#########################################
##########       Layouts      ###########
#########################################


layouts = [
    # layout.Columns(),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(),
     layout.Bsp(
        border_focus= colors[2],
        border_normal= colors[1],
        border_width=3, 
        single_border_width=0,
        highlight_color= colors[8],
        highlight_method="border",
         ),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.Columns(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]



#########################################
###########    Widgets   ################
#########################################


widget_defaults = dict(
    #font="TerminessNerdFont Bold",
    #font="OverpassM Nerd Font",
    font="IntoneMono Nerd Font",
    #font="MonaspiceKr Nerd Font",

    fontsize=16,
    padding=5,
)

extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [

            
widget.Spacer(length=10,),

            
            widget.GroupBox(
                fontsize = 28,
                margin_y = 5,
                margin_x = 5,
                padding_y = 0,
                padding_x = 4,
                borderwidth = 3,
                active = colors[4],
                inactive = colors[1],
                rounded = False,
                highlight_color = colors[0],
                highlight_method = "line",
                this_current_screen_border = colors[2],
                this_screen_border = colors [5],
                other_current_screen_border = colors[5],
                other_screen_border = colors[8],
                ),


            widget.TextBox(
                text = '|',
                font = "JetBrainsMono Nerd Font",
                foreground = colors[7],
                padding = 2,
                fontsize = 14
                ),


#            widget.CurrentLayoutIcon(
#                foreground = colors[1],
#                padding = 4,
#                scale = 0.5,
#                ),
#
#            widget.TextBox(
#                text = '|',
#                font = "JetBrainsMono Nerd Font",
#                foreground = colors[1],
#                padding = 2,
#                fontsize = 14
#                ),


            widget.TextBox(
                text = "󱦞",
                foreground = colors[2],
                padding = 4,
                fontsize = 18
                ),


            widget.WindowName(
                foreground = colors[1],
                max_chars = 25,
                padding=10,
                ),


            widget.Wlan(
                interface="wlan1",
                format="  {essid}",
                foreground= colors[1],  
                padding=5,
                decorations=[
                    BorderDecoration(
                    colour=colors[1],
                    border_width=[0, 0, 2, 0],
                    )
                    ]
                ),


widget.Spacer(length = 8),


         widget.Battery(
                format='BAT: {percent:1.0%} {char}',
                charge_char='',
                discharge_char='',
                show_short_text=False,
                foreground=colors[2],
                update_interval=10,
                padding=5,
                decorations=[
                BorderDecoration(
                colour=colors[2],
                border_width=[0, 0, 2, 0],
                 ),
             ]
            ),
	
widget.Spacer(length = 8),


            widget.GenPollText(
            func=cpu_info,
            update_interval=20,
            foreground=colors[3],
            decorations=[
                BorderDecoration(
                    colour=colors[3],
                    border_width=[0, 0, 2, 0],
                        )
                    ],
                ),

#widget.CPU(
#                format = '  {load_percent}%',
#                foreground = colors[3],
#                    decorations=[
#                    BorderDecoration(
#                    colour = colors[3],
#                    border_width = [0, 0, 2, 0],
#                    )
#                    ]
#                ),

widget.Spacer(length = 7),


            widget.Memory(
                foreground = colors[4],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                format='{MemUsed:.1f}GB',
                measure_mem='G',
                fmt = ' {}',
                    decorations=[
                    BorderDecoration(
                    colour = colors[4],
                    border_width = [0, 0, 2, 0],
                    )
                    ],
                ),


 widget.Spacer(length = 9),


            widget.DF(
                update_interval = 60,
                foreground = colors[5],
                partition = '/',
                format='{uf}{m}B',
                fmt = '  {}',
                visible_on_warn = False,
				measure_units='GB',
                    decorations=[
                    BorderDecoration(
                    colour = colors[5],
                    border_width = [0, 0, 2, 0],
                    )
                    ]
                ),


 widget.Spacer(length = 9),


            widget.KeyboardLayout(
                foreground = colors[6],
                fmt = ' :{}',
                    decorations=[
                    BorderDecoration(
                    colour = colors[6],
                    border_width = [0, 0, 2, 0],
                    )
                    ]
                ),


widget.Spacer(length = 9),


            widget.Volume(
                foreground = colors[7],
                fmt = '󰕾 {}',
                    decorations=[
                    BorderDecoration(
                    colour = colors[7],
                    border_width = [0, 0, 2, 0],
                    )
                    ]
                ),


widget.Spacer(length = 9),


            widget.Clock(
                foreground = colors[8],
                format = "  %H:%M |   %d %B %A",
                    decorations=[
                    BorderDecoration(
                    colour = colors[8],
                    border_width = [0, 0, 2, 0],
                    )
                    ]
                ),


widget.Spacer(length = 9),


                widget.Systray(padding = 3),


            ],
            28,
            background= colors[0],
        #     border_width=[8, 5, 3, 8],  # Draw top and bottom borders
        #     border_color=["#000000", "#2f4e91", "#3e944a", "#000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # x11_drag_polling_rate = 60
    ),
]
###widgets and bar settings are end here##



#drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]



##FLOATING RULES##
floating_layout = layout.Floating(
	border_focus= colors[4],
	border_normal= colors[5],
	border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"), 
        Match(wm_class="makebranch"),  
        Match(wm_class="maketag"),  
        Match(wm_class="ssh-askpass"), 
        Match(title="branchdialog"), 
        Match(title="pinentry"),  
        Match(title="Calculator"),
    ]
)



#a few more settings for window management
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []



# If things like steam games want to auto-minimize themselves when losing focus, should we respect this or not? (if you set on 'True', u probably gonna fucked up)
auto_minimize = False



#wmname = "LG3D"
wmname = "overnormal's wm"
