from pathlib import Path
import json
from html import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.colors import HexColor
from PIL import Image
R=Path(__file__).resolve().parents[1];d=json.loads((R/'content.json').read_text())
for n,f in [('Body','Arial.ttf'),('Bold','Arial Bold.ttf')]:pdfmetrics.registerFont(TTFont(n,'/System/Library/Fonts/Supplemental/'+f))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold')
W,H=842,595;c=canvas.Canvas(str(R/'downloads/Venkata_Ganji_Case_Studies.pdf'),pagesize=(W,H));c.setTitle('Venkata Ganji | Engineering Architecture Case Studies');c.setAuthor('Venkata Ganji')
ink='#19332f';muted='#52675f';teal='#126c60'
def txt(x,y,s,size=10,bold=False,color=ink):c.setFillColor(HexColor(color));c.setFont('Bold' if bold else 'Body',size);c.drawString(x,H-y,s)
def p(x,y,s,width=365,size=10.3,bold=False,color=ink):
 st=ParagraphStyle('p',fontName='Bold' if bold else 'Body',fontSize=size,leading=size*1.38,textColor=HexColor(color));v=Paragraph(escape(s),st);_,h=v.wrap(width,1000);v.drawOn(c,x,H-y-h);return y+h+9
page=0
def start(kicker,title):
 global page;page+=1;c.setFillColor(HexColor('#f7f8f3'));c.rect(0,0,W,H,fill=1,stroke=0);c.setFillColor(HexColor(teal));c.rect(0,H-7,W,7,fill=1,stroke=0);txt(35,35,kicker,9,True,teal);txt(35,69,title,25,True);txt(35,574,'Venkata Ganji | Architecture portfolio | offroadguy.github.io',8,color=muted);txt(794,574,str(page),8,color=muted);c.linkURL('https://offroadguy.github.io/',(35,12,425,31),relative=0)
start('ENGINEERING PORTFOLIO / OCTOBER 2026','AI infrastructure and distributed systems')
y=p(35,100,'Venkata Ganji',width=750,size=30,bold=True);y=p(35,y+8,d['intro'],width=730,size=17)
for i,a in enumerate(d['cases']):
 yy=240+i*67;txt(35,yy,a['number'],14,True,teal);txt(75,yy,a['short'],17,True);p(75,yy+10,a['engagement'],width=720,size=10,color=muted);c.linkURL('https://offroadguy.github.io/cases/'+a['id']+'.html',(35,H-yy-35,810,H-yy+20),relative=0)
p(35,522,'Sanitized reconstructions and career-reported outcomes. Full case studies and supporting diagrams are available on the website.',width=760,size=9,color=muted);c.showPage()
for a in d['cases']:
 start('CASE '+a['number']+' / '+a['category'],a['short'])
 txt(35,91,a['engagement'].replace('·','|'),9,color=muted)
 y=p(35,113,a['summary'],width=770,size=11)
 for i,(v,l) in enumerate(a['metrics']):
  x=35+i*263;txt(x,y+22,v,23,True,teal);p(x,y+31,l,width=246,size=8.7,color=muted)
 top=y+80;y1=p(35,top,'What I owned',size=14,bold=True)
 for t in a['ownership']:y1=p(35,y1,'• '+t,width=365,size=10)
 y2=p(442,top,'Engineering decisions',size=14,bold=True)
 for title,t in a['decisions']:
  y2=p(442,y2,title,width=365,size=10,bold=True);y2=p(442,y2-5,t,width=365,size=9.7,color=muted)
 low=max(y1,y2)+2
 if low>515:raise RuntimeError((a['id'],'overflow',low))
 p(35,low,'Scope: '+a['scope'],width=770,size=8.1,color=muted)
 c.showPage()
 start('CASE '+a['number']+' / ARCHITECTURE',a['short'])
 f=R/'.build'/(a['diagram']+'.png');im=Image.open(f);w,h=im.size;scale=min(770/w,450/h);ww,hh=w*scale,h*scale;c.drawImage(str(f),35+(770-ww)/2,H-100-hh,ww,hh,mask='auto')
 url='https://offroadguy.github.io/cases/'+a['id']+'.html';txt(35,555,'Explore the full-size diagram, system flow, results and supporting views online →',9,True,teal);c.linkURL(url,(35,32,805,51),relative=0);c.showPage()
c.save();print('Created 9-page case-study pack')
