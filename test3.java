using 'std'
using 'colorama'

let (auto) arr = [1,2,3,4,5]
let (auto) new_arr = []


forin (arr -> val) {
    std.append(new_arr, val*2)
}
out(colorama.fore.green, new_arr, colorama.fore.resset)
