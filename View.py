import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Controller import PersonService
from Model import PersonRepository

class NationalCodeCheckerApp:
    def __init__(self, root):
        self.service = PersonService(PersonRepository())
        self.root = root
        self.root.title("بررسی کد ملی")
        self.root.geometry("400x250")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="کد ملی:", font=("Vazir", 12)).pack(pady=10)
        self.code_entry = ttk.Entry(self.root, width=35)
        self.code_entry.pack(pady=5)
        ttk.Button(self.root, text="بررسی", bootstyle=PRIMARY, command=self.check_code).pack(pady=10)
        self.result_label = ttk.Label(self.root, text="", font=("Vazir", 10))
        self.result_label.pack(pady=5)

    def check_code(self):
        code = self.code_entry.get().strip()
        if not code:
            self.result_label.config(text="❗ لطفاً کد ملی را وارد کنید.")
            return
        if self.service.is_code_valid(code):
            self.result_label.config(text="خوش آمدید")
        else:
            self.result_label.config(text="❌ کد ملی پیدا نشد.")
