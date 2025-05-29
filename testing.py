from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class MyApp(App):
    """A simple TUI application."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Static("Hello, TUI World!")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_quit(self) -> None:
        """An action to quit the app."""
        self.exit()

if __name__ == "__main__":
    app = MyApp()
    app.run()