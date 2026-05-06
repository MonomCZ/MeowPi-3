from input.base import InputHandler

class KeyboardInput(InputHandler):
    def get_event(self):
        key = input("w/s/a/d/e: ")
        if key =='w':
            return {"type": "PRESS", "key": "UP"}
        elif key == "s":
            return {"type": "PRESS", "key": "DOWN"}
        elif key == "a":
            return {"type": "PRESS", "key": "BACK"}
        elif key == "d":
            return {"type": "PRESS", "key": "SELECT"}
        elif key == "e":
            return {"type": "PRESS", "key": "MODE"}
        return None
    

