import base64, hashlib

class Encode:
    
    @staticmethod
    def sha256_hash(path_file):
        with open(path_file, "rb") as f:
            bytes = f.read()
            readable_hash = hashlib.sha256(bytes).hexdigest()
            return str(readable_hash)

    @staticmethod
    def base64_encode(path_file):
        with open(path_file, "rb") as img_file:
            b64_string = base64.b64encode(img_file.read()).decode('utf-8')
            return b64_string
    
    @staticmethod
    def md5_hash(path_file):
        md5_hash = hashlib.md5()
        a_file = open(path_file, "rb")
        content = a_file.read()
        md5_hash.update(content)
        digest = md5_hash.hexdigest()
        return str(digest)
