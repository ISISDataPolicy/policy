# ISIS Neutron and Muon Source Data Policy

This is a Github repository for tracking revisions of the ISIS Data Policy.

The latest version is available on the ISIS website from https://www.isis.stfc.ac.uk/Pages/Data-Policy.aspx.

## Working With The Repository

It is recommended that [Visual Studio Code](https://code.visualstudio.com/)
with the [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
extension be used to edit the policy. If `Format on Save` is enabled then the
extension will automatically fix any issues with the document such as extraneous
whitespace or bare external links.

A [GitHub Action workflow](./.github/workflows/cichecks.yml) is defined to check
the documents when opening a pull request or pushing to the default branch.
