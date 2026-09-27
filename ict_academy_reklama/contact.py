import sys,glob
from PIL import Image
fs=sorted(glob.glob('kadrlar/*.png'), key=lambda f: float(f.split('_')[1][:-4]))
W=270;H=480;cols=6;rows=(len(fs)+cols-1)//cols
im=Image.new('RGB',(W*cols,H*rows))
for i,f in enumerate(fs): im.paste(Image.open(f).convert('RGB').resize((W,H)),((i%cols)*W,(i//cols)*H))
im.save(sys.argv[1])
