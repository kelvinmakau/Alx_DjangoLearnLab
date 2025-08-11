# Authentication System

## Features

- User registration with username, email, and password
- Login and Logout using Django's auth views
- Profile page for editing email

## URLS

/register - Create an account
/login    - Log in to the site
/logout   - Log out
/profile  - View and edit your profile

## Security

- CSRF tokens on all forms
- Passwords hashed using Django’s authentication system

## Blog Post Features ## URLS

- /posts/          -> list
  - /posts/new/      -> create (login required)
  - /posts/<pk>/     -> detail
  - /posts/<pk>/edit/-> edit (author only)
  - /posts/<pk>/delete/ -> delete (author only)
- Only the post author can edit/delete.
- Forms use PostForm; author is set automatically in CreateView.
