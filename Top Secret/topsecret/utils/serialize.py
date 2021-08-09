from itsdangerous.url_safe import URLSafeSerializer
from itsdangerous.exc import BadTimeSignature, SignatureExpired, BadSignature

def serialize(data):
    token = URLSafeSerializer(data)
    return token.dumps(data)