class Question:
    def __init__(self, text: str, answer: str):
        # Con 2 underscore rendiamo la variabile privata
        self.__text = text
        self.__answer = answer

    def get_text(self) -> str:
        return self.__text

    def get_answer(self) -> str:
        return self.__answer
