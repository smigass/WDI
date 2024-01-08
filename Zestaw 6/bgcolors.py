class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def blue(self, text):
        return self.OKBLUE + text + self.ENDC

    def green(self, text):
        return self.OKGREEN + text + self.ENDC

    def header(self, text):
        return self.HEADER + text + self.ENDC

    def bold(self, text):
        return self.BOLD + text + self.ENDC

    def fail(self, text):
        return self.FAIL + text + self.ENDC

    def yellow(self, text):
        return self.WARNING + text + self.ENDC
