def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" Ogiltig inmatning. Ange ett heltal.")
