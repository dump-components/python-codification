import base64

class Decode:
    
    @staticmethod
    def decode_base64(name_file, base_64) -> tuple:
        binary_file = base64.b64decode(base_64)
        return (name_file, binary_file)