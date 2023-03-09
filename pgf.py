from turbo_colormap import interpolate_or_clip, turbo_colormap_data

f = open("pgf.tex", "w")

print("\\pgfplotsset{colormap={turbo}{", file=f)

use_all_pts = False
npts = len(turbo_colormap_data) if use_all_pts else 20

for i in range(npts):
   if use_all_pts:
      rgb = turbo_colormap_data[i]
   else:
      pos = i/(npts-1.)
      rgb = interpolate_or_clip(turbo_colormap_data, pos)
   a = 255
   print("   rgb=({:.2f},{:.2f},{:.2f})".format(*rgb), file=f)

print("}}", file=f)

f.close()
