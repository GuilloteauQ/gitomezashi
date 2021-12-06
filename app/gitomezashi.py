"""
Hitomezashi Stitch Patterns for git commit hashes
"""
from git import Repo
import os
import cairosvg
import svgwrite
import sys

def get_hash(repo_path):
    """
    returns the current commit hash
    """
    repo = Repo(repo_path)
    head_commit = repo.head.commit
    return head_commit.hexsha

def split_hash(commit_hash):
    """
    split the hash in half
    """
    mid = 20
    return (commit_hash[:mid], commit_hash[mid:])

def hex_to_bin(hexcode):
    """
    returns the bin representation of the hexcode
    """
    return bin(int(hexcode, 16)).zfill(20 * 4)

def flip(coords, do_flip):
    """
    flip coords
    """
    return (coords[1], coords[0]) if do_flip else coords

def draw_line(stitch,
              horizontal,
              is_vertical,
              config):
    """
    draw the horizontal parts
    """
    step = config["x_step"] if is_vertical else config["y_step"]
    y_position = 0
    for current_bit in horizontal:
        start = 0
        end = 80 * step
        if current_bit == '0':
            start += step
            end += 1
        for x_position in range(start, end, 2 * step):
            stitch.add(stitch.line(flip((x_position, y_position), is_vertical),
                                   flip((x_position + step, y_position), is_vertical),
                                   stroke=config["color"],
                                   stroke_width=config["stroke_width"]))
        y_position += step

def draw_svg(horizontal, vertical, config):
    """
    draw the svg
    """
    x_step = config["x_step"]
    y_step = config["y_step"]
    stitch = svgwrite.Drawing(config["filename"],
                              profile="full",
                              size=(
                                  f"{x_step * 80}mm",
                                  f"{y_step * 80}mm"
                              ))
    stitch.viewbox(
        width=x_step * 80,
        height=y_step * 80
    )
    stitch.add(stitch.rect((0, 0), (x_step * 80, y_step * 80), fill="white"))

    draw_line(stitch, vertical, True, config)
    draw_line(stitch, horizontal, False, config)

    stitch.save()

def main():
    """
    main function
    """
    args = sys.argv
    if len(args) > 1:
        repo_path = sys.argv[1]
    else:
        repo_path = os.getcwd()
    commit_hash = get_hash(repo_path)
    (left, right) = split_hash(commit_hash)
    vertical = hex_to_bin(left)
    horizontal = hex_to_bin(right)
    config = {
        "filename": "commit.svg",
        "outname": "commit.png",
        "x_step": 2,
        "y_step": 2,
        "stroke_width": 1,
        "color": "black",
        "dpi": 50
    }
    draw_svg(horizontal, vertical, config)
    cairosvg.svg2png(url=config["filename"], write_to=config["outname"], dpi=config["dpi"])
    if os.path.exists(config["filename"]):
        os.remove(config["filename"])

    return 0

if __name__ == "__main__":
    main()
