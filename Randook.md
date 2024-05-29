import re

# حمولة Whitespace ( شيفرة شل متغيرة )
whitespace_payload = """
[LF][Tab][LF][Tab][Tab][LF][Tab][Tab][Tab][LF][Tab][Tab][Tab][Tab][LF]
[Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab]
[LF][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab]
[Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab]
"""

# كود بايثون لاستخراج وتنفيذ حمولة Whitespace
def extract_payload(code):
    payload = ""
    for char in code:
        if char in ["\t", "\n", " "]:
            payload += char
    return payload

def execute_payload(payload):
    # تنفيذ حمولة Whitespace
    exec(payload)

# مثال للاستخدام
python_code = """
print("Hello, World!")
"""
whitespace_code = extract_payload(whitespace_payload)
execute_payload(whitespace_code)
