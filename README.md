# ISIS Neutron and Muon Source Data Policy

This is a Github repository for tracking revisions of the ISIS Data Policy.

The latest version is available on the ISIS website from https://www.isis.stfc.ac.uk/Pages/Data-Policy.aspx.

## Working With The Repository

It is recommended that [Visual Studio Code](https://code.visualstudio.com/)
with the [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
extension be used to edit the policy. If `Format on Save` is enabled then the
extension will automatically fix any issues with the document such as extraneous
whitespace or bare external links. This check is also part of a
[GitHub Action workflow](./.github/workflows/cichecks.yml) check
the documents when opening a pull request or pushing to the default branch.

The action also has an additional check for dead external links using
[markdown-link-check](https://github.com/marketplace/actions/markdown-link-check).

## Creating a New Version

To create a new version of the policy:

1. Create a branch and make the required changes to the document.
2. Check, and update if necessary, the [.zenodo metadata](./.zenodo.json).
3. Open a pull request to merge to the default branch.
4. Send an email to the review group asking for any further comments and provide a link
   to the pull request plus a word copy of the document as it would look for those without
   GitHub access. Ask for feedback within 1 month.
5. Once all feedback has been processed and the final changes to the document have been made
   the pull request can be merged.
6. Create a new GitHub release, including a bullet list of the major changes in the description.
7. Once published check [Zenodo](https://zenodo.org/account/settings/github/repository/ISISDataPolicy/policy)
   has created a fresh DOI.
8. Finally, update the policy on the public ISIS website.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3827816.svg)](https://doi.org/10.5281/zenodo.3827816)
