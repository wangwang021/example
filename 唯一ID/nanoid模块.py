# pip install nanoid
from nanoid import generate

# 使用 URL 友好的符号 (A-Za-z0-9_-) 并返回一个 21 个字符的 ID
print(generate())

# 减少 ID 长度（并增加冲突概率），您可以将长度作为参数传递。
print(generate(size=10))

# 自定义字母或长度
print(generate(alphabet="1234567890abcdefg", size=10))
