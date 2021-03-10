# ISIS Neutron and Muon Source Data Policy

This is a Github reposity for editing, updating and keeping revisions of the ISIS Data Policy.

Available from the ISIS website from https://www.isis.stfc.ac.uk/Pages/Data-Policy.aspx .

The data policy is available in both markdown and JSON formats. The `format_converter.py` script can be used to convert between them, so changes can be made to whichever is more convenient. The JSON version of the policy is in the format:

```
{
    "preamble": string,
    "sections": [section]
}

section = {
    "heading": string,
    "content": [ string | section ]
}
```
