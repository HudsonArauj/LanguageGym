class PrePro:
    @staticmethod
    def filter(code):
        return code.replace("\n", " ").replace(";", "")
