class WriteLetter:
    def __init__(self, template_path, names_path, to_send_path):
        self.template_path = template_path
        self.names_path = names_path
        self.to_send_path = to_send_path
        self.template = self.read_template()

    def write_letter(self):
        for name in self.read_names():
            personalized_letter = self.replace_name(self.template, name.strip())
            with open(f"{self.to_send_path}{name.strip()}.txt", "w") as ready_to_send:
                ready_to_send.write(personalized_letter)

    def read_template(self):
        with open(self.template_path) as template:
            temp_letter = template.read()
        return temp_letter

    def read_names(self):
        with open(self.names_path) as names_list:
            names = names_list.readlines()
        return names

    @staticmethod
    def replace_name(line, name):
        return line.replace("[name]", name.strip())

