from handright import Template,handwrite
from PIL import ImageFont, ImageDraw
from PIL import Image

with open("article.txt",encoding='utf-8') as f:
    text=f.read()
background = Image.open('北航红色抬头信纸.jpg')

height=background.height
width=background.width

template=Template(
    background=background,
    font=ImageFont.truetype("PingFangZhuiGuangTi-2.ttf",size=70),
    line_spacing=115,fill=0,
    left_margin=130,
    top_margin=460,
    bottom_margin=230,
    right_margin=100,
    word_spacing=6,
    line_spacing_sigma=0.5,
    font_size_sigma=3,
    word_spacing_sigma=1,
    end_chars="，。",
    perturb_x_sigma=1,
    perturb_y_sigma=1,
    perturb_theta_sigma=0.06
)
images=handwrite(text,template)
i=1
for im in images:
    assert isinstance(im,Image.Image)
    im.show()
    im.save("pic{}.jpg".format(i))
    i+=1
