# pip install ascii-magic

import ascii_magic
output = ascii_magic.from_image("1.jpg")
output.to_html_file('ascii_art.html',columns = 300,width_ratio =2)


