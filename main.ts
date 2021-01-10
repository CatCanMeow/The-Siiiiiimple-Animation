let Animation_Elements = [images.arrowImage(ArrowNames.North), images.arrowImage(ArrowNames.NorthEast), images.arrowImage(ArrowNames.East), images.arrowImage(ArrowNames.SouthEast), images.arrowImage(ArrowNames.South), images.arrowImage(ArrowNames.SouthWest), images.arrowImage(ArrowNames.West), images.arrowImage(ArrowNames.NorthWest), images.createImage(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `), images.iconImage(IconNames.Sad), images.iconImage(IconNames.No), images.createImage(`
    # . # . #
    . # . # .
    # . # . #
    . # . # .
    # . # . #
    `), images.createImage(`
    . # . # .
    # . # . #
    . # . # .
    # . # . #
    . # . # .
    `), images.createImage(`
    # . # . #
    . # . # .
    # . # . #
    . # . # .
    # . # . #
    `), images.createImage(`
    . # . # .
    # . # . #
    . # . # .
    # . # . #
    . # . # .
    `), images.createImage(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)]
basic.forever(function () {
    for (let Element_Image of Animation_Elements) {
        Element_Image.showImage(0)
    }
})
