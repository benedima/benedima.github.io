# Martin Benedict · portfolio

An experience-first personal website for https://benedima.github.io.

Warm white, forest green, serif headings and an original SVG data-flow illustration follow the visual concept. The content hierarchy takes inspiration from Brittany Chiang's concise experience-focused portfolio; no code, imagery or copy is taken from her website.

## Preview before publishing

No Node dependencies or build step are needed. Open `index.html` in a browser, or serve the repository locally:

```sh
python -m http.server 8000 --bind 127.0.0.1
```

On Windows, `py -m http.server 8000 --bind 127.0.0.1` also works. Visit http://localhost:8000. Stop with Ctrl+C.

To preview this PR, clone the repository and check out its branch first:

```sh
git clone https://github.com/benedima/benedima.github.io.git
cd benedima.github.io
git checkout feature/experience-portfolio
```

After merging, use `main` for subsequent work. Test at 375px, 768px and desktop widths in browser developer tools, at 200% zoom, and using only the keyboard. Check navigation, focus visibility, CV and LinkedIn links and printing.

## Publishing

The site is static and compatible with GitHub Pages branch publishing. In Settings → Pages, use **Deploy from a branch**, **main**, **/(root)**. The repository already has Pages enabled; verify its source setting before merging. Merging to the configured publishing branch updates the live site. This PR does not change repository settings or deploy a preview.

The included workflow validates the HTML and local references on PRs and main pushes. It does not deploy. Public repository branches are publicly readable, even before the site is published.

## Editing

- `index.html`: introduction, experience, About, skills and contact links.
- `assets/styles.css`: colours, layouts, mobile and print styles.
- `assets/favicon.svg`: browser icon.

The site works without JavaScript, external fonts, analytics or third-party embeds. Experience is visible in the initial HTML.

The CV link opens the PDF currently committed in the separate CV repository. It is labelled **View full CV**, not a guaranteed download or automatically generated release. Replace its URL if you choose a different public CV. LinkedIn is taken from the CV repository's profile configuration.

Content uses concise career-level descriptions from the CV and the owner's supplied experience. Detailed consent rules, legal exceptions, production schemas and internal incident material are deliberately excluded. Review public-facing wording and metrics before merging. Keep future unpublished case studies out of public commits.

## Validation

Run `python scripts/check_site.py`. CI runs the same check plus the Nu HTML validator. Browser visual review remains necessary; source checks cannot verify visual layout.
