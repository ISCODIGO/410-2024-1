class ColorTerminal:
    RESET_COLOR = "\033[0m"  # Resetear color a default
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    @staticmethod
    def cprint(msg: str, color):
        print(f"{color}{msg}{ColorTerminal.RESET_COLOR}")

    @staticmethod
    def to_str(msg: str, color):
        return f"{color}{msg}{ColorTerminal.RESET_COLOR}"
