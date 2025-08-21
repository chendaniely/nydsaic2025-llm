def input_approval(prompt: str) -> bool:
    while True:
        res = input(f"{prompt} (yes/no): ")
        if res.lower() in ["yes", "y"]:
            return True
        elif res.lower() in ["no" or "n"]:
            return False
        else:
            print("Please answer with 'yes' or 'no'.")
