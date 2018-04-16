import tulip

class Pager(tulip.VContainer):
    def __init__(self, children):
        super().__init__(children)
        self.vscroll = 0
        self.hscroll = 0

    def _render(self, screen, y, x, i, j, rows, cols):
        return super()._render(screen, y, x, i + self.vscroll, j + self.hscroll, rows, cols)

    def next_page(self):
        rows, _ = self.size
        self.vscroll = max(0, min(self.vscroll + self.last_render_rows, rows - 1))

    def prev_page(self):
        self.vscroll = max(self.vscroll - self.last_render_rows, 0)