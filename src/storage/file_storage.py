from storage.base_storage import BaseStorage
import os


class FileStorage(BaseStorage):
    def save(self, content, path):
        try:
            directory = os.path.dirname(path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(path, "w") as file:
                file.write(content)
        except IOError as e:
            print(f"An error occurred while saving file {path}: {e}")

    def set_up_folders(self, depth: int):
        for i in range(depth + 1):
            os.makedirs(str(i), exist_ok=True)
