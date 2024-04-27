using 'gl'
using 'std'

const (list) win_size = [1000, 700]

gl.window.create(win_size, 'test')
gl.window.set.maxfps(60)

let (int) radius = randint(20,100)
let (auto) posx = randint(radius, win_size[0]-radius)
let (auto) posy = randint(radius, win_size[1]-radius)

let (auto) speedx = randint(-10,10)
let (auto) speedy = randint(-10,10)

let (bool) stoped = false

fn (list) random_color() {
    return -> [
        randint(0,255),
        randint(0,255),
        randint(0,255),
    ]
}
let (list) color = random_color()

let (list) ccs = []

while gl.loop() {
    gl.events.update()
    gl.window.viewfps()
    
    stoped = false
    if gl.math.distance(gl.mouse.pos(), [posx, posy])<radius{
        let (auto) c = [255,0,0]
        if gl.mouse.press.left(){
            stoped = true
        }
    } else {
        let (auto) c = color
    }
    if stoped <> true {
        posx = posx + speedx
        posy = posy + speedy
    }
    forin (ccs -> circle){
        if gl.math.distance(circle, [posx, posy]) < radius+30{
            let (auto) c = [255,0,0]
            break ->
        }

    }

    if (posx-radius<0 || posx+radius>win_size[0]) {speedx = speedx * -1}
    if (posy-radius<0 || posy+radius>win_size[1]) {speedy = speedy * -1}

    gl.draw.circle([posx, posy], radius, c)

    if gl.mouse.click.right(){
        std.append(ccs, gl.mouse.pos())
    }

    forin (ccs -> circle){
        gl.draw.circle(circle, 30, 'green')
    }
}
