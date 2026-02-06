# Configurable Keybindings

ttydal now supports configurable keybindings! You can customize all navigation and action keys to match your preferences.

## Configuration File

Keybindings are stored in `~/.ttydal/config.json` under the `keybindings` section.

Run `ttydal --init-config` to create the config file with default keybindings. The app works without a config file (uses bundled defaults).

## Configuration Structure

The keybindings configuration is organized by component:

```json
{
  "keybindings": {
    "navigation": {
      "cursor_down": "down",
      "cursor_up": "up",
      "cursor_left": "left",
      "cursor_right": "right"
    },
    "app": {
      "show_player": "p",
      "show_config": "c",
      "focus_albums": "a",
      "focus_tracks": "t",
      "open_search": "/",
      "open_cache_info": "i",
      "toggle_play": "space",
      "toggle_auto_play": "n",
      "toggle_shuffle": "s",
      "toggle_vibrant_color": "v",
      "seek_backward": "shift+left",
      "seek_forward": "shift+right",
      "play_previous": "P",
      "play_next": "N",
      "quit": "q"
    },
    "player_page": {
      "toggle_playback": "space"
    },
    "albums_list": {
      "refresh_albums": "r"
    },
    "tracks_list": {
      "play_selected_track": "enter",
      "refresh_tracks": "r"
    },
    "search_modal": {
      "close_modal": "escape",
      "select_result": "enter",
      "play_track": "space"
    },
    "cache_modal": {
      "close_modal": "escape"
    },
    "login_modal": {
      "open_url": "o",
      "copy_url": "c",
      "check_login": "l",
      "close_modal": "escape"
    },
    "config_page": {
      "toggle_switch": "space"
    }
  }
}
```

## Customizing Keybindings

1. Open `~/.ttydal/config.json` in your text editor
2. Find the `keybindings` section
3. Change any key value to your preferred key
4. Save the file
5. Restart ttydal

## Key Format

Keys can be specified in several formats:

- **Single keys**: `"a"`, `"p"`, `"1"`, `"space"`, `"enter"`, `"escape"`
- **Modified keys**: `"shift+left"`, `"ctrl+c"`, `"alt+a"`
- **Special keys**: `"up"`, `"down"`, `"left"`, `"right"`, `"tab"`, `"backspace"`

### Common Special Key Names

- `space` - Spacebar
- `enter` - Enter/Return
- `escape` - Escape key
- `tab` - Tab key
- `backspace` - Backspace
- `delete` - Delete key
- `up`, `down`, `left`, `right` - Arrow keys
- `home`, `end` - Home/End keys
- `pageup`, `pagedown` - Page Up/Down

### Modifiers

Combine keys with modifiers using `+`:
- `shift+` - Shift key modifier
- `ctrl+` - Control key modifier
- `alt+` - Alt key modifier

Examples:
- `"shift+left"` - Shift + Left Arrow
- `"ctrl+c"` - Control + C
- `"alt+enter"` - Alt + Enter

## Example Customizations

### Vim-style Navigation

```json
{
  "navigation": {
    "cursor_down": "j",
    "cursor_up": "k",
    "cursor_left": "h",
    "cursor_right": "l"
  }
}
```

### Arrow-based Seeking

```json
{
  "app": {
    "seek_backward": "left",
    "seek_forward": "right",
    "play_previous": "up",
    "play_next": "down"
  }
}
```

### Custom Modal Controls

```json
{
  "search_modal": {
    "close_modal": "q",
    "select_result": "o",
    "play_track": "p"
  }
}
```

## Troubleshooting

### My changes aren't working

1. Make sure you saved the config file
2. Restart ttydal completely
3. Check that the JSON is valid (no syntax errors)
4. Ensure the key names are spelled correctly

### The config file doesn't exist

Run `ttydal --init-config` to create it with default values.

### I want to reset to defaults

Run `ttydal --init-config --force` to overwrite your config with the bundled defaults.

## Available Actions by Component

### Navigation (Global)
These keys control cursor movement in lists and other navigable elements. Change to `j`/`k`/`h`/`l` for vim-style navigation.
- `cursor_down` - Move cursor down in lists
- `cursor_up` - Move cursor up in lists
- `cursor_left` - Move focus left (e.g., tracks → albums)
- `cursor_right` - Move focus right (e.g., albums → tracks)

### App (Global)
- `show_player` - Switch to player view
- `show_config` - Switch to config view
- `focus_albums` - Focus the albums list
- `focus_tracks` - Focus the tracks list
- `open_search` - Open fuzzy search modal
- `open_cache_info` - Open cache info modal
- `toggle_play` - Play/pause current track
- `toggle_auto_play` - Toggle auto-play next track
- `toggle_shuffle` - Toggle shuffle mode
- `toggle_vibrant_color` - Toggle vibrant album colors
- `seek_backward` - Seek backward 10 seconds
- `seek_forward` - Seek forward 10 seconds
- `play_previous` - Play previous track
- `play_next` - Play next track
- `quit` - Quit the application

### Player Page
- `toggle_playback` - Alternative play/pause binding

### Albums List
- `refresh_albums` - Refresh the albums list

### Tracks List
- `play_selected_track` - Play the selected track
- `refresh_tracks` - Refresh the tracks list

### Config Page
- `toggle_switch` - Toggle switch controls (default: space)

### Search Modal
- `close_modal` - Close the search modal
- `select_result` - Navigate to selected album
- `play_track` - Play selected track

### Cache Modal
- `close_modal` - Close the cache info modal

### Login Modal
- `open_url` - Open login URL in browser
- `copy_url` - Copy login URL to clipboard
- `check_login` - Check if login completed
- `close_modal` - Close the login modal
