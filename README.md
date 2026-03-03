# Y12-DTP
A repository of projects that I have made in Year 12.

## car_brands_app
This Flask micro‑app uses a local SQLite database named `brands.db` that
should live in the same directory as `app.py`.  The application computes the
path using `app.root_path` so it will continue working regardless of the
current working directory.  If you ever see a ``FileNotFoundError`` complaining
about the database path, verify that the file is present or update
`app.config['DATABASE']` accordingly.
