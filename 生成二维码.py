import qrcode

url = 'https://www.qq.com'
img = qrcode.make(url, error_correction=qrcode.constants.ERROR_CORRECT_H)
img.show()
