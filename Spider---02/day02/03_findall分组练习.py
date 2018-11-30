import re 

s = """<div class="animal">
  <p class="name">
    <a title="Tiger"></a>
  </p>
  
  <p class="contents">
    Two tigers two tigers run fast
  </p>
</div>

<div class="animal">
  <p class="name">
    <a title="Rabbit"></a>
  </p>
  
  <p class="contents">
    Small white rabbit white and white 
  </p>
</div>"""

p = re.compile('<div class="animal".*?title="\
        (.*?)">.*?contents">(.*?)</p>',re.S)
r = p.findall(s)
#print(r)
for animal in r:
    print("动物名称:",animal[0].strip())
    print("动物描述:",animal[1].strip())















#[("Tiger","Two tiger ..."),
# ("Rabbit","Small Rabbit ...")]
#
## 打印输出
#动物名称 ：Tiger
#动物描述 ：Two tigers ...








  
  
  
  
  
  
  
  
  
  
  
  
  