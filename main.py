Animation_Elements = [images.arrow_image(ArrowNames.NORTH),
    images.arrow_image(ArrowNames.NORTH_EAST),
    images.arrow_image(ArrowNames.EAST),
    images.arrow_image(ArrowNames.SOUTH_EAST),
    images.arrow_image(ArrowNames.SOUTH),
    images.arrow_image(ArrowNames.SOUTH_WEST),
    images.arrow_image(ArrowNames.WEST),
    images.arrow_image(ArrowNames.NORTH_WEST),
    images.create_image("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """),
    images.icon_image(IconNames.SAD),
    images.icon_image(IconNames.NO),
    images.create_image("""
    # . # . #
    . # . # .
    # . # . #
    . # . # .
    # . # . #
    """),
    images.create_image("""
    . # . # .
    # . # . #
    . # . # .
    # . # . #
    . # . # .
    """),
    images.create_image("""
    # . # . #
    . # . # .
    # . # . #
    . # . # .
    # . # . #
    """),
    images.create_image("""
    . # . # .
    # . # . #
    . # . # .
    # . # . #
    . # . # .
    """)]

def on_forever():
    for Element_Image in Animation_Elements:
        Element_Image.show_image(0)
basic.forever(on_forever)
