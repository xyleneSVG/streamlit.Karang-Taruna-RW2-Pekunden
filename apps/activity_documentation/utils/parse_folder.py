def parse_folder_name(name):
    if " | " in name:
        activity, date = name.split(" | ")
        return activity, date
    return name, "-"