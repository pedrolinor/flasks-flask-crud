class Task:
    def __init__(self, id, tittle,  description, done=False) -> None:
        self.id = id
        self.tittle = tittle
        self.description = description
        self.done = done

    def to_dict(self):
        return {
            "id": self.id,
            "tittle": self.tittle,
            "description": self.description,
            "done": self.done
        }

