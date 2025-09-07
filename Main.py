import ttkbootstrap as ttk
from View import NationalCodeCheckerApp

if __name__ == "__main__":
    app = ttk.Window(themename="flatly")
    NationalCodeCheckerApp(app)
    app.mainloop()
