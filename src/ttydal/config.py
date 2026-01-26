"""Configuration manager for ttydal.

Manages application configuration stored in ~/.ttydal/config.json
"""

import json
from pathlib import Path
from typing import Any


class ConfigManager:
    """Singleton configuration manager for ttydal."""

    _instance = None

    def __new__(cls):
        """Ensure only one instance exists."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Initialize the config manager."""
        if self._initialized:
            return

        self.config_dir = Path.home() / ".ttydal"
        self.config_file = self.config_dir / "config.json"
        self._config: dict[str, Any] = {}
        self._load_config()
        self._initialized = True

    def _get_default_keybindings(self) -> dict[str, dict[str, str]]:
        """Get default keybindings configuration."""
        return {
            "navigation": {
                "cursor_down": "down",
                "cursor_up": "up",
                "cursor_left": "left",
                "cursor_right": "right",
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
                "quit": "q",
            },
            "player_page": {
                "toggle_playback": "space",
            },
            "albums_list": {
                "refresh_albums": "r",
            },
            "tracks_list": {
                "play_selected_track": "enter",
                "refresh_tracks": "r",
            },
            "search_modal": {
                "close_modal": "escape",
                "select_result": "enter",
                "play_track": "space",
            },
            "cache_modal": {
                "close_modal": "escape",
            },
            "login_modal": {
                "open_url": "o",
                "copy_url": "c",
                "check_login": "l",
                "close_modal": "escape",
            },
            "config_page": {
                "toggle_switch": "space",
            },
        }

    def _merge_default_keybindings(self) -> None:
        """Merge any missing keybindings from defaults into user config."""
        defaults = self._get_default_keybindings()
        changed = False

        if "keybindings" not in self._config:
            self._config["keybindings"] = defaults
            changed = True
        else:
            user_bindings = self._config["keybindings"]

            # Add missing components
            for component, actions in defaults.items():
                if component not in user_bindings:
                    user_bindings[component] = actions
                    changed = True
                else:
                    # Add missing actions within existing components
                    for action, key in actions.items():
                        if action not in user_bindings[component]:
                            user_bindings[component][action] = key
                            changed = True

        if changed:
            self._save_config()

    def _load_config(self) -> None:
        """Load configuration from file or create default config."""
        self.config_dir.mkdir(parents=True, exist_ok=True)

        if self.config_file.exists():
            with open(self.config_file, "r") as f:
                self._config = json.load(f)

            # Merge in any missing keybindings from defaults
            self._merge_default_keybindings()
        else:
            # Default configuration
            self._config = {
                "theme": "rose-pine",
                "quality": "high",  # high or low
                "auto_play": True,  # auto-play next track when current finishes
                "debug_logging_enabled": False,  # enable debug logging to ~/.ttydal/debug.log
                "api_logging_enabled": False,  # enable API request/response logging to ~/.ttydal/debug-api.log
                "keybindings": self._get_default_keybindings(),
            }
            self._save_config()

    def _save_config(self) -> None:
        """Save configuration to file."""
        with open(self.config_file, "w") as f:
            json.dump(self._config, f, indent=2)

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value and save."""
        self._config[key] = value
        self._save_config()

    @property
    def theme(self) -> str:
        """Get the current theme."""
        return self.get("theme", "textual-dark")

    @theme.setter
    def theme(self, value: str) -> None:
        """Set the current theme."""
        self.set("theme", value)

    @property
    def quality(self) -> str:
        """Get the audio quality setting."""
        return self.get("quality", "high")

    @quality.setter
    def quality(self, value: str) -> None:
        """Set the audio quality setting."""
        if value not in ("max", "high", "low"):
            raise ValueError("Quality must be 'max', 'high', or 'low'")
        self.set("quality", value)

    @property
    def auto_play(self) -> bool:
        """Get the auto-play setting."""
        return self.get("auto_play", True)

    @auto_play.setter
    def auto_play(self, value: bool) -> None:
        """Set the auto-play setting."""
        self.set("auto_play", value)

    @property
    def debug_logging_enabled(self) -> bool:
        """Get the debug logging enabled setting."""
        return self.get("debug_logging_enabled", True)

    @debug_logging_enabled.setter
    def debug_logging_enabled(self, value: bool) -> None:
        """Set the debug logging enabled setting."""
        self.set("debug_logging_enabled", value)

    @property
    def api_logging_enabled(self) -> bool:
        """Get the API logging enabled setting."""
        return self.get("api_logging_enabled", True)

    @api_logging_enabled.setter
    def api_logging_enabled(self, value: bool) -> None:
        """Set the API logging enabled setting."""
        self.set("api_logging_enabled", value)

    @property
    def shuffle(self) -> bool:
        """Get the shuffle setting."""
        return self.get("shuffle", False)

    @shuffle.setter
    def shuffle(self, value: bool) -> None:
        """Set the shuffle setting."""
        self.set("shuffle", value)

    @property
    def vibrant_color(self) -> bool:
        """Get the vibrant color setting (colorize player bar with album's vibrant color)."""
        return self.get("vibrant_color", False)

    @vibrant_color.setter
    def vibrant_color(self, value: bool) -> None:
        """Set the vibrant color setting."""
        self.set("vibrant_color", value)

    def get_keybinding(self, component: str, action: str) -> str:
        """Get a keybinding for a specific component and action.

        Args:
            component: Component name (e.g., "app", "player_page", "albums_list")
            action: Action name (e.g., "show_player", "toggle_play")

        Returns:
            Key binding string (e.g., "p", "space", "shift+left")
        """
        keybindings = self.get("keybindings", {})
        defaults = self._get_default_keybindings()

        # Get key from user config, fall back to default if not found
        user_key = keybindings.get(component, {}).get(action)
        if user_key is not None:
            return user_key

        # Fall back to default
        return defaults.get(component, {}).get(action, "")
