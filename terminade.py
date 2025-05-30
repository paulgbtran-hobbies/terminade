from os import system

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static, Button, Input 

class Main(App):
    TITLE = 'TerminaDE'
    SUB_TITLE = 'Start'
    CSS_PATH = 'styles.tcss'
    BINDINGS = [
        ('a', 'apps', 'Apps'),
        ('u', 'utils', 'Utilities'),
        ('f', 'files', 'Files'),
        ('s', 'settings', 'Settings'),
        ('v', 'version', 'Version'),
        ('e', 'exit', 'Exit')
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static('Use the keybinds below to start.', id='startmsg')

    def action_apps(self) -> None: pass

    def action_files(self) -> None: pass

    def action_settings(self) -> None: pass
    
    def action_version(self) -> None: pass

    def action_exit(self) -> None: self.exit(self)



if __name__ == '__main__': Main().run()