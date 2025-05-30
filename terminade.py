from os import system

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static, Markdown, Button, DirectoryTree, Input, MarkdownViewer

class FileMan(Container):
    def on_mount(self) -> None:
        self.mount(DirectoryTree('/'))
        self.mount(Input())
        

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

    def action_files(self) -> None: 
        # with self.suspend(): system('python3 terminade_fileman.py')
        if len(self.query('#fileman')) == 0:
            startmsg = self.query('#startmsg')
            if len(startmsg) == 1: startmsg.remove()

            fileman = Container(FileMan(), id='fileman')
            self.mount(fileman)
        else:
            fileman = self.query_one('#fileman')
            if fileman: 
                fileman.remove()
                self.mount(Static('Use the keybinds below to start.', id='startmsg'))


    def action_settings(self) -> None: pass
    
    def action_version(self) -> None:
        startmsg = self.query('#startmsg')
        if len(startmsg) == 1: startmsg.remove()

        if len(self.query('#version')) == 0:
            text = '''TerminaDE
Version 0.0.1
Authored by Paul Tran.'''
            version = Static(text, id='version')
            self.mount(version)
        else:
            version = self.query_one('#version')
            if version: 
                version.remove()
                self.mount(Static('Use the keybinds below to start.', id='startmsg'))

    def action_exit(self) -> None: self.exit(self)

if __name__ == '__main__': Main().run()