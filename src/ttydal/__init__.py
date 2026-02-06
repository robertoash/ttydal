"""ttydal - Tidal in your terminal!"""

import argparse
import sys
import traceback
from ttydal.logger import log
from ttydal.config import ConfigManager


def main() -> None:
    """Launch the ttydal TUI application."""
    parser = argparse.ArgumentParser(description="Tidal in your terminal!")
    parser.add_argument(
        "--init-config",
        action="store_true",
        help="Copy the default config to ~/.ttydal/config.json",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing config (use with --init-config)",
    )
    args = parser.parse_args()

    if args.init_config:
        try:
            path = ConfigManager.init_config(force=args.force)
            print(f"Config created at {path}")
        except FileExistsError as e:
            print(e, file=sys.stderr)
            sys.exit(1)
        return

    from ttydal.app import TtydalApp

    log("="*80)
    log("Starting ttydal application")
    log("="*80)

    app = None
    try:
        log("Creating TtydalApp instance...")
        app = TtydalApp()
        log("TtydalApp instance created successfully")

        log("Starting app.run()...")
        app.run()
        log("App.run() completed normally")
    except KeyboardInterrupt:
        log("Received KeyboardInterrupt (Ctrl+C)")
    except Exception as e:
        log(f"ERROR: Exception caught in main: {e}")
        log(f"Exception type: {type(e).__name__}")
        log("Full traceback:")
        log(traceback.format_exc())

        print(f"Error starting ttydal: {e}", file=sys.stderr)
        traceback.print_exc()
        sys.exit(1)
    finally:
        log("Performing final cleanup...")
        if app is not None:
            try:
                # Ensure player is shutdown
                if hasattr(app, 'player'):
                    log("  - Final player shutdown check...")
                    app.player.shutdown()
            except Exception as e:
                log(f"  - Error during final cleanup: {e}")
        log("Application exited")
        log("="*80)

