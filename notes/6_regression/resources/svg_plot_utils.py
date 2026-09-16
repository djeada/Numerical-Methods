"""Small dependency-light SVG helpers used by the regression-note plotting scripts."""
from html import escape
from pathlib import Path
import numpy as np

PALETTE = ["#2563eb", "#dc2626", "#059669", "#7c3aed", "#d97706", "#0891b2", "#4b5563"]

def _fmt(v):
    if abs(v) >= 1000 or (0 < abs(v) < 1e-3):
        return f"{v:.1e}"
    return f"{v:.3g}"

def _bounds(series, scatter):
    xs, ys = [], []
    for item in list(series) + list(scatter):
        xs.extend(np.asarray(item["x"], float).ravel())
        ys.extend(np.asarray(item["y"], float).ravel())
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    if xmin == xmax:
        xmin, xmax = xmin - 1, xmax + 1
    if ymin == ymax:
        ymin, ymax = ymin - 1, ymax + 1
    px = 0.06 * (xmax - xmin)
    py = 0.10 * (ymax - ymin)
    return xmin-px, xmax+px, ymin-py, ymax+py

def line_chart(path, title, xlabel, ylabel, series=(), scatter=(), xlim=None, ylim=None,
               max_points=140, legend_below=False):
    """Draw an SVG; max_points=None preserves every supplied curve sample."""
    path = Path(path)
    W, H = 800, 450
    L, R, T, B = 82, 28, 54, 68
    legend_count = sum(bool(item.get("label")) for item in list(series) + list(scatter))
    extra_height = 24 * ((legend_count + 1) // 2) if legend_below else 0
    canvas_height = H + extra_height
    xmin, xmax, ymin, ymax = _bounds(series, scatter)
    if xlim:
        xmin, xmax = xlim
    if ylim:
        ymin, ymax = ylim
    def X(x):
        return L + (np.asarray(x)-xmin)/(xmax-xmin)*(W-L-R)
    def Y(y):
        return T + (ymax-np.asarray(y))/(ymax-ymin)*(H-T-B)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{canvas_height}" viewBox="0 0 {W} {canvas_height}">',
           '<rect width="100%" height="100%" fill="white"/>',
           f'<text x="{W/2}" y="28" text-anchor="middle" font-family="sans-serif" font-size="18">{escape(title)}</text>']
    for i in range(5):
        tx = xmin + i*(xmax-xmin)/4
        ty = ymin + i*(ymax-ymin)/4
        px, py = float(X(tx)), float(Y(ty))
        out.append(f'<line x1="{px:.2f}" y1="{T}" x2="{px:.2f}" y2="{H-B}" stroke="#e5e7eb"/>')
        out.append(f'<line x1="{L}" y1="{py:.2f}" x2="{W-R}" y2="{py:.2f}" stroke="#e5e7eb"/>')
        out.append(f'<text x="{px:.2f}" y="{H-B+22}" text-anchor="middle" font-family="sans-serif" font-size="11">{_fmt(tx)}</text>')
        out.append(f'<text x="{L-10}" y="{py+4:.2f}" text-anchor="end" font-family="sans-serif" font-size="11">{_fmt(ty)}</text>')
    out += [f'<line x1="{L}" y1="{T}" x2="{L}" y2="{H-B}" stroke="#111827" stroke-width="1.2"/>',
            f'<line x1="{L}" y1="{H-B}" x2="{W-R}" y2="{H-B}" stroke="#111827" stroke-width="1.2"/>',
            f'<text x="{(L+W-R)/2}" y="{H-18}" text-anchor="middle" font-family="sans-serif" font-size="13">{escape(xlabel)}</text>',
            f'<text x="20" y="{(T+H-B)/2}" transform="rotate(-90 20 {(T+H-B)/2})" text-anchor="middle" font-family="sans-serif" font-size="13">{escape(ylabel)}</text>']
    legend = []
    for k, item in enumerate(series):
        xs, ys = np.asarray(item["x"], float), np.asarray(item["y"], float)
        if max_points is not None and len(xs) > max_points:
            idx = np.linspace(0, len(xs)-1, max_points).astype(int)
            xs, ys = xs[idx], ys[idx]
        pts = " ".join(f"{x:.2f},{y:.2f}" for x,y in zip(X(xs),Y(ys)))
        color = item.get("color", PALETTE[k % len(PALETTE)])
        dash = item.get("dash", "")
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        out.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2.2"{dash_attr}/>')
        if item.get("label"):
            legend.append((color, item["label"], dash))
    for k, item in enumerate(scatter):
        xs, ys = np.asarray(item["x"], float), np.asarray(item["y"], float)
        color = item.get("color", PALETTE[(k+len(series)) % len(PALETTE)])
        for x,y in zip(X(xs),Y(ys)):
            out.append(f'<circle cx="{float(x):.2f}" cy="{float(y):.2f}" r="4" fill="{color}" stroke="white" stroke-width="1"/>')
        if item.get("label"):
            legend.append((color, item["label"], ""))
    if legend:
        x0, y0 = (L, H + 4) if legend_below else (W-R-210, T+8)
        if not legend_below:
            out.append(f'<rect x="{x0-8}" y="{y0-16}" width="210" height="{24*len(legend)+10}" rx="4" fill="white" fill-opacity=".88" stroke="#d1d5db"/>')
        for i,(color,label,dash) in enumerate(legend):
            x0 = L + (i % 2) * 345 if legend_below else W-R-210
            y = y0 + (i // 2 if legend_below else i)*24
            dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
            out.append(f'<line x1="{x0}" y1="{y}" x2="{x0+26}" y2="{y}" stroke="{color}" stroke-width="2.2"{dash_attr}/>')
            out.append(f'<text x="{x0+34}" y="{y+4}" font-family="sans-serif" font-size="11">{escape(label)}</text>')
    out.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out), encoding="utf-8")

def heatmap(path, title, x, y, z, points=None):
    path = Path(path)
    x, y, z = np.asarray(x), np.asarray(y), np.asarray(z)
    W, H = 680, 520
    L, R, T, B = 72, 95, 50, 55
    zmin, zmax = float(np.min(z)), float(np.max(z))
    def color(v):
        t = 0.5 if zmax == zmin else (v-zmin)/(zmax-zmin)
        r = int(35 + 210*t)
        g = int(90 + 80*(1-abs(2*t-1)))
        b = int(220 - 170*t)
        return f"rgb({r},{g},{b})"
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         '<rect width="100%" height="100%" fill="white"/>',
         f'<text x="{W/2}" y="27" text-anchor="middle" font-family="sans-serif" font-size="18">{escape(title)}</text>']
    nx, ny = z.shape[1], z.shape[0]
    cw, ch = (W-L-R)/nx, (H-T-B)/ny
    for j in range(ny):
        for i in range(nx):
            out.append(f'<rect x="{L+i*cw:.2f}" y="{T+(ny-1-j)*ch:.2f}" width="{cw+0.2:.2f}" height="{ch+0.2:.2f}" fill="{color(float(z[j,i]))}"/>')
    if points is not None:
        p=np.asarray(points)
        xmin,xmax=float(np.min(x)),float(np.max(x))
        ymin,ymax=float(np.min(y)),float(np.max(y))
        for px,py in p:
            sx=L+(px-xmin)/(xmax-xmin)*(W-L-R)
            sy=T+(ymax-py)/(ymax-ymin)*(H-T-B)
            out.append(f'<circle cx="{sx:.2f}" cy="{sy:.2f}" r="4" fill="white" stroke="#111827" stroke-width="1.5"/>')
    for k in range(5):
        yy=T+k*(H-T-B)/4
        v=zmax-k*(zmax-zmin)/4
        out.append(f'<rect x="{W-64}" y="{yy:.2f}" width="14" height="{(H-T-B)/4+1:.2f}" fill="{color(v)}"/>')
        out.append(f'<text x="{W-44}" y="{yy+4:.2f}" font-family="sans-serif" font-size="10">{_fmt(v)}</text>')
    out.append("</svg>")
    path.write_text("\n".join(out),encoding="utf-8")

def wireframe(path, title, x, y, z, points=None):
    path=Path(path)
    x=np.asarray(x); y=np.asarray(y); z=np.asarray(z)
    W,H=760,500
    def proj(xv,yv,zv):
        sx=360 + 190*xv - 120*yv
        sy=300 - 65*xv - 55*yv - 105*zv
        return sx,sy
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         '<rect width="100%" height="100%" fill="white"/>',
         f'<text x="{W/2}" y="28" text-anchor="middle" font-family="sans-serif" font-size="18">{escape(title)}</text>']
    step=max(1,z.shape[0]//12)
    for j in range(0,z.shape[0],step):
        pts=" ".join(f"{proj(float(x[j,i]),float(y[j,i]),float(z[j,i]))[0]:.1f},{proj(float(x[j,i]),float(y[j,i]),float(z[j,i]))[1]:.1f}" for i in range(z.shape[1]))
        out.append(f'<polyline points="{pts}" fill="none" stroke="#2563eb" stroke-width="1" stroke-opacity=".7"/>')
    for i in range(0,z.shape[1],step):
        pts=" ".join(f"{proj(float(x[j,i]),float(y[j,i]),float(z[j,i]))[0]:.1f},{proj(float(x[j,i]),float(y[j,i]),float(z[j,i]))[1]:.1f}" for j in range(z.shape[0]))
        out.append(f'<polyline points="{pts}" fill="none" stroke="#059669" stroke-width="1" stroke-opacity=".7"/>')
    if points is not None:
        for px,py,pz in np.asarray(points):
            sx,sy=proj(float(px),float(py),float(pz))
            out.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="4" fill="#dc2626" stroke="white"/>')
    out += ['<text x="600" y="415" font-family="sans-serif" font-size="12">x</text>',
            '<text x="140" y="390" font-family="sans-serif" font-size="12">y</text>',
            '<text x="370" y="70" font-family="sans-serif" font-size="12">s(x,y)</text>',
            '</svg>']
    path.write_text("\n".join(out),encoding="utf-8")
