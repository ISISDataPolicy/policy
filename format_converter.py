import json
import re
from typing import List, Tuple
from pprint import pprint


def to_md(file_name):
    with open(file_name, "r") as f:
        d = json.load(f)
    heading_markers = re.findall("#+", d["preamble"])
    preamble_heading_level = max([len(h) for h in heading_markers], default=0)

    section_texts = []
    for section_num, section in enumerate(d["sections"]):
        section_texts.append(
            build_section_text(
                section,
                [str(section_num + 1)],
                preamble_heading_level + 1))
        section_texts.append("")

    return d["preamble"] + "\n".join(section_texts)


def build_section_text(section, section_numbering, heading_level):
    header = f'{"#" * heading_level} {".".join(section_numbering)} {section["heading"]}'
    sub_sections = [header, ""]
    for item_num, item in enumerate(section["content"]):
        item_numbering = section_numbering + [str(item_num + 1)]
        if "heading" in item:
            sub_sections.append(
                build_section_text(item, item_numbering, heading_level + 1))
        else:
            sub_sections.append(f'{".".join(item_numbering)} {item}')
        sub_sections.append("")
    return "\n".join(sub_sections)


def to_dict(file_name):
    preamble, body = read_md(file_name)
    return {
        "preamble": preamble,
        "sections": SectionBuilder(body).build_section_list()
    }
 

def read_md(file_name) -> Tuple[str, List[str]]:
    reading_preamble = True
    preamble_lines = []
    body_lines = []
    with open(file_name, "r") as f:
        for line in f:
            if reading_preamble:
                if "1." in line:
                    reading_preamble = False
                else:
                    preamble_lines.append(line)
            if not reading_preamble and line.strip():
                m = re.search("(?P<section_num>(\d+\.)+\d*)\s+(?P<content>.+)", line)
                if not m:
                    print(f"md line was in unexpected format: '{line}'")
                else:
                    nums = m.group("section_num").split(".")
                    nesting_level = len([n for n in nums if n])
                    body_lines.append((nesting_level, m.group("content")))

    return "".join(preamble_lines), body_lines


class SectionBuilder:
    def __init__(self, body):
        self.c = 0
        self.body = body

    def build_section_list(self):
        sections = []
        while self.c < len(self.body):
            sections.append(self.build_section())
            self.c += 1
        return sections

    @property
    def next_nest_level(self):
        return self.body[self.c + 1][0] if self.c + 1 < len(self.body) else None

    @property
    def cur_is_heading(self):
        return self.next_nest_level is not None and self.next_nest_level > self.body[self.c][0]

    def build_section(self):
        heading_nest, heading = self.body[self.c]
        content = []
        while self.next_nest_level is not None and self.next_nest_level > heading_nest:
            self.c += 1
            if self.cur_is_heading:
                content.append(self.build_section())
            else:
                content.append(self.body[self.c][1])
        return {
            "heading": heading,
            "content": content,
        }

if __name__ == "__main__":
    with open("test.json", "w") as f:
        json.dump(to_dict("data_policy.md"), f, indent=2)

    with open("test.md", "w") as f:
        f.write(to_md("test.json"))
