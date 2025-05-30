from textual.app import App, ComposeResult
from textual.widgets import Header,Footer, DirectoryTree, Input

class FileMan(App):

    BINDINGS = [
        ('b', 'back', 'Back to Start')
    ]
    TITLE = 'TerminaDE'
    SUB_TITLE = 'File Manager'

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield DirectoryTree('./')
        yield Input(type='text')

    def action_back(self) -> None: self.exit(self)

if __name__ == '__main__': FileMan().run()